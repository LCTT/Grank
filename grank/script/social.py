from ..libs import query
from ..libs import helpers
import pandas as pd
import numpy as np
import click
import math
import re

def analyse_email(data,config):
    if config["social"]["askrule"] != '1':
        return False

    click.echo("邮件域分布：")
    # 邮箱匹配规则
    regex_rule = re.compile('@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?')
    ignore_mail = ['@users.noreply.github.com','']
    df = pd.DataFrame(data["commitArray"])

    for index,row in df.iterrows():
        df.loc[index,"domain"] = helpers.detect_email_domain(row["author"])

    click.echo(df['domain'].value_counts().drop(labels=ignore_mail,errors='ignore'))

    new_rule = click.prompt('请输入新的社区化识别的正则规则：',default=config["social"]["rule"])
    if new_rule != '':
        if new_rule == '!':
            config["social"]["askrule"] = '0'
            click.echo('不再询问规则！')
        else:
            config["social"]["rule"] = new_rule
            click.echo('规则设置完成！')
    
    pass

def analyse_repo(owner, repository, data, config):
    click.echo("开始社区化分析：%s/%s" % (owner, repository))
    pullRequestArray = data["pullRequestArray"]
    commitArray = data["commitArray"]

    start_time = config["time"]["start_time"]
    end_time = config["time"]["end_time"]
    date_range = pd.date_range(start=start_time, end=end_time, freq="W")
    date_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)

    social_all_frame = pd.DataFrame(commitArray)
    for index,row in social_all_frame.iterrows():
        social_all_frame.loc[index,"domain"] = helpers.detect_email_domain(row["author"])
        
    social_all_frame = social_all_frame[(social_all_frame.domain != '') & (social_all_frame.domain != '@users.noreply.github.com') & (social_all_frame.date != "未标注时间")]
    social_all_frame["date"] = pd.to_datetime(social_all_frame['date'])
    for index, row in social_all_frame.iterrows():
        social_all_frame.loc[index, "is_corp"] = helpers.is_corp(
            row["domain"], config)

    community_df = social_all_frame[social_all_frame.is_corp != True].set_index(
        'date').resample('W')['times'].sum()
    social_all_df = social_all_frame.set_index(
        'date').resample('W')['times'].sum()

    social_all_df = social_all_df.loc[start_time:end_time]
    community_df = community_df.loc[start_time:end_time]

    temp_community_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)
    temp_social_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)

    for item in community_df.index:
        if item in date_series.index:
            temp_community_series[item] = community_df[item]

    for item in social_all_df.index:
        if item in date_series.index:
            temp_social_series[item] = social_all_df[item]

    social_df = pd.DataFrame({
        "community_member": temp_community_series.values,
        "all_member": temp_social_series.values,
    }, index=date_range)
    social_df = social_df.cumsum()
    social_df["score"] = social_df.apply(
        lambda row: row.community_member / row.all_member, axis=1)

    target_social_score = social_df["score"].mean()

    instance = helpers.get_social_average_instance()

    helpers.export_pickle(social_df, 'social', owner, repository)

    helpers.set_social_average(
        instance, owner, repository, target_social_score)

    helpers.export_csv(social_df,  'social', owner, repository)

    click.echo("%s/%s 的平均社区化程度为 %.2f%%" %
               (owner, repository, 100 * target_social_score))
    
    return social_df

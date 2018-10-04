from ..libs import query
from ..libs import helpers
import pandas as pd
import numpy as np
import click
import math


def analyse_repo(owner, repository, data, config):
    click.echo("========= Community start =========")
    click.echo("开始进行社区化分析：%s/%s" % (owner, repository))
    pullRequestArray = data["pullRequestArray"]
    commitArray = data["commitArray"]

    start_time = config["time"]["start_time"]
    end_time = config["time"]["end_time"]
    date_range = pd.date_range(start=start_time, end=end_time, freq="W")
    date_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)

    social_all_frame = pd.DataFrame(commitArray)
    social_all_frame = social_all_frame[social_all_frame.date != "未标注时间"]
    social_all_frame["date"] = pd.to_datetime(social_all_frame['date'])
    for index, row in social_all_frame.iterrows():
        social_all_frame.loc[index, "author"] = helpers.is_corp(
            row["author"], config)

    community_df = social_all_frame[social_all_frame.author != True].set_index(
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

    target_social_score = social_df["score"].sum() / len(social_df)

    instance = helpers.get_social_average_instance()

    helpers.series_to_pickle(social_df, "social_%s" % repository)

    helpers.set_social_average(
        instance, owner, repository, target_social_score)

    helpers.export_csv(social_df, "social_%s" % repository)

    helpers.generate_social_line_number(
        start_time, end_time, int(config["rank"]["top"]))

    click.echo("输出成功 %s/%s 的社区化分数为 %.2f" %
               (owner, repository, target_social_score))
    click.echo("排行榜及折线图请查看 result 目录下的 social_line.png 和 social_rank.csv")
    pass

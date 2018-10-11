from ..libs import helpers
import pandas as pd
import numpy as np
import click
import math


def analyse_repo(owner, repository, data, config):
    """查询 Repo 数据"""
    click.echo("========= Activity start =========")
    pullRequestArray = data["pullRequestArray"]
    commitArray = data["commitArray"]

    start_time = config["time"]["start_time"]
    end_time = config["time"]["end_time"]
    top_number = int(config["rank"]["top"])
    date_range = pd.date_range(start=start_time, end=end_time, freq="W")
    date_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)

    click.echo("分析 PR")
    pr_frame = pd.DataFrame(pullRequestArray)
    if not pr_frame.empty:
        pr_frame = pr_frame[pr_frame.date != "未标注时间"]
        pr_frame["date"] = pd.to_datetime(pr_frame['date'])
        pr_dstList = pr_frame.set_index('date').resample('W')['times'].sum()
        pr_dstList = pr_dstList.loc[start_time:end_time]

    click.echo("分析 Commit")

    commit_frame = pd.DataFrame(commitArray)
    commit_frame = commit_frame[commit_frame.date != "未标注时间"]
    commit_frame["date"] = pd.to_datetime(commit_frame['date'])
    commit_dstList = commit_frame.set_index(
        'date').resample('W')['times'].sum()
    commit_dstList = commit_dstList.loc[start_time:end_time]

    click.echo("分析 Contributor")
    contributor_frame = pd.DataFrame(commitArray)
    contributor_frame = contributor_frame[contributor_frame.date != "未标注时间"]
    contributor_frame["date"] = pd.to_datetime(contributor_frame['date'])
    contributor_dstList = contributor_frame.drop_duplicates(
        subset=["author"]).set_index('date').resample('W')['times'].sum()
    contributor_dstList = contributor_dstList.loc[start_time:end_time]

    new_commit_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)
    for item in commit_dstList.index:
        if item in date_series.index:
            new_commit_series[item] = commit_dstList[item]

    new_pr_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)
    for item in pr_dstList.index:
        if item in date_series.index:
            new_pr_series[item] = pr_dstList[item]

    new_contributor_series = pd.Series(
        np.zeros((len(date_range),), dtype=int), index=date_range)
    for item in contributor_dstList.index:
        if item in date_series.index:
            new_contributor_series[item] = contributor_dstList[item]

        # 构成新的 DataFrame

    new_df = pd.DataFrame({
        "contributor": new_contributor_series.values,
        "commit": new_commit_series.values,
        "pr": new_pr_series.values
    }, index=date_range)

    # 计算活跃分数

    new_df["score"] = new_df.apply(lambda row: math.sqrt(
        row.pr*row.pr + row.contributor * row.contributor + row.commit*row.commit), axis=1)

    # 求活跃分数平均值

    target_score = new_df["score"].sum() / len(new_df)

    # 获取平均分实例，用于后续排序

    instance = helpers.get_activity_average_instance()

    # 将项目的活跃分数保存到新的 Pickle 中，用于后续的折线图输出

    helpers.export_pickle(new_df, 'activity', owner, repository)

    # 对平均分实例进行排序

    helpers.set_activity_average(instance, owner, repository, target_score)

    # 输出项目的 CSV 数据
    helpers.export_csv(new_df, 'activity', owner, repository)

    click.echo("输出成功,%s 旗下的 %s 项目的活跃分数为 %.2f" %
               (owner, repository, target_score))

    return new_df

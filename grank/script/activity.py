from ..libs import query
from ..libs import helpers
import pandas as pd
import numpy as np
import click
import math
def analyse_repo(owner,repository,config):
    """查询 Repo 数据"""
    # 定义空白数组
    commitArray = []
    pullRequestArray = []

    # 添加一个可过滤掉的数据，确保后续执行完成
    commitArray.append({
            'author' : 'localhost',
            'date': '未标注时间',
            "times":1
        })
    pullRequestArray.append({
            'date': '未标注时间',
            "times":1
        })
    # 定义查询变量
    start_time=config["time"]["start_time"]
    end_time=config["time"]["end_time"]
    top_number=int(config["rank"]["top"])
    click.echo("初次抓取数据:%s/%s" % (owner,repository))
    # 进行初次查询
    all_query = query.all_query % (owner, repository)
    result = helpers.query(all_query,config)
    # 生成时间 Series
    date_range = pd.date_range(start=start_time,end=end_time,freq="W")
    date_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)

    # 处理第一组数据
    if (helpers.has_result(result,"commit")):
        for commit in result["data"]["repository"]["ref"]["target"]["history"]["edges"]:
            helpers.add_item_to_commit_array(commit,commitArray)
            pass
    if (helpers.has_result(result,"pr")):
        for pullRequest in result["data"]["repository"]["pullRequests"]["nodes"]:
            helpers.add_item_to_pr_array(pullRequest,pullRequestArray)

    while helpers.has_next_page(result,"commit") or helpers.has_next_page(result,"issue") or helpers.has_next_page(result,"pr"):
        click.echo("继续抓取数据:%s/%s" % (owner,repository));
        if (helpers.has_result(result,"commit")):
            for commit in result["data"]["repository"]["ref"]["target"]["history"]["edges"]:
                helpers.add_item_to_commit_array(commit,commitArray)
                pass
        if (helpers.has_result(result,"pr")):
            for pullRequest in result["data"]["repository"]["pullRequests"]["nodes"]:
                helpers.add_item_to_pr_array(pullRequest,pullRequestArray)

        if (helpers.has_next_page(result,"pr") and helpers.has_next_page(result,"commit")):
            next_query = query.all_query_with_pager % (owner,repository,helpers.get_page_cursor(result,"pr"),helpers.get_page_cursor(result,"commit"))
        elif (helpers.has_next_page(result,"pr")):
            next_query = query.pr_query_with_pager % (owner,repository,helpers.get_page_cursor(result,"pr"))
        elif (helpers.has_next_page(result,"commit")):
            next_query = query.commit_query_with_pager % (owner,repository,helpers.get_page_cursor(result,"commit"))

        result = helpers.query(next_query,config)

    print("分析 PR")
    pr_frame = pd.DataFrame(pullRequestArray);
    if not pr_frame.empty:
        pr_frame = pr_frame[pr_frame.date != "未标注时间"]
        pr_frame["date"] = pd.to_datetime(pr_frame['date'])
        pr_dstList = pr_frame.set_index('date').resample('W')['times'].sum()
        pr_dstList = pr_dstList.loc[start_time:end_time]

    print("分析 commit")

    commit_frame = pd.DataFrame(commitArray);

    # commit_frame.to_pickle("output/commits.pkl")
    commit_frame = commit_frame[commit_frame.date != "未标注时间"]
    commit_frame["date"] = pd.to_datetime(commit_frame['date'])
    commit_dstList = commit_frame.set_index('date').resample('W')['times'].sum()
    commit_dstList = commit_dstList.loc[start_time:end_time]

    print("分析 Contributor")
    contributor_frame = pd.DataFrame(commitArray);

    contributor_frame = contributor_frame[contributor_frame.date != "未标注时间"]
    contributor_frame["date"] = pd.to_datetime(contributor_frame['date'])
    contributor_dstList = contributor_frame.drop_duplicates(subset=["author"]).set_index('date').resample('W')['times'].sum()
    contributor_dstList = contributor_dstList.loc[start_time:end_time]


    new_commit_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in commit_dstList.index:
        if item in date_series.index:
            new_commit_series[item] = commit_dstList[item]


    new_pr_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in pr_dstList.index:
        if item in date_series.index:
            new_pr_series[item] = pr_dstList[item]


    new_contributor_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in contributor_dstList.index:
        if item in date_series.index:
            new_contributor_series[item] = contributor_dstList[item]

        # 构成新的 DataFrame

    new_df = pd.DataFrame({
        "contributor":new_contributor_series.values,
        "commit":new_commit_series.values,
        "pr":new_pr_series.values
    },index = date_range)

    # 计算活跃分数

    new_df["score"] = new_df.apply(lambda row: math.sqrt(row.pr*row.pr + row.contributor * row.contributor + row.commit*row.commit), axis=1)

    # 求活跃分数平均值

    target_score = new_df["score"].sum() / len(new_df)

    # 获取平均分实例，用于后续排序

    instance = helpers.get_avarage_instance()

     # 将项目的活跃分数保存到新的 Pickle 中，用于后续的折线图输出

    helpers.series_to_pickle(new_df,repository)

    # 对平均分实例进行排序

    helpers.set_avarage(instance,repository,target_score)

    # 输出项目的 CSV 数据
    helpers.export_csv(new_df,"%s" % repository)

    # 生成折线图

    helpers.generate_line_number(start_time,end_time,top_number)
    click.echo("输出成功,%s 旗下的 %s 项目的活跃分数为 %.15f"% (owner,repository,target_score))
    click.echo("排行榜及折线图请查看 result 目录")


def analyse_organ(organization,config):
    repositoryArray = []
    click.echo("开始抓取组织数据:%s" % organization)
    all_query = query.organ_all_query % organization
    result = helpers.query(all_query,config)
    if (helpers.has_result(result,'repository')):
            for repo in result["data"]["organization"]["repositories"]["nodes"]:
                if repo['stargazers']["totalCount"] > 100:
                    repositoryArray.append({"owner":organization,"repository":repo["name"]})

    while(helpers.has_next_page(result,'repository')):
        click.echo("继续抓取组织数据: %s" % organization)
        if (helpers.has_result(result,'repository')):
            for repo in result["data"]["organization"]["repositories"]["nodes"]:
                if repo['stargazers']["totalCount"] > 100:
                    repositoryArray.append({"owner":organization,"repository":repo["name"]})

        click.echo("继续抓取组织数据:%s" % organization)
        next_query = query.organ_all_query_with_pager % (organization,helpers.get_page_cursor(result,"repository"))
        result = helpers.query(next_query,config)

    for item in repositoryArray:
        analyse_repo(item["owner"],item["repository"],config)

def analyse_user(user,config):
    repositoryArray = []
    click.echo("开始抓取用户数据:%s" % user)
    all_query = query.user_all_query % user
    result = helpers.query(all_query,config)
    if (helpers.has_result(result,'user_repository')):
            for repo in result["data"]["user"]["repositories"]["nodes"]:
                if repo['stargazers']["totalCount"] > 100:
                    repositoryArray.append({"owner":user,"repository":repo["name"]})

    while(helpers.has_next_page(result,'user_repository')):
        click.echo("继续抓取组织数据: %s" % organization)
        if (helpers.has_result(result,'user_repository')):
            for repo in result["data"]["user"]["repositories"]["nodes"]:
                if repo['stargazers']["totalCount"] > 100:
                    repositoryArray.append({"owner":user,"repository":repo["name"]})

        click.echo("继续抓取用户数据:%s" % user)
        next_query = query.organ_all_query_with_pager % (organization,helpers.get_page_cursor(result,"user_repository"))
        result = helpers.query(next_query,config)

    for item in repositoryArray:
        analyse_repo(item["owner"],item["repository"],config)


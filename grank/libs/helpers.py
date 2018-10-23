import requests
import os
import configparser
import datetime
import click
import re
import pandas as pd
import matplotlib
import math

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def query(query, config):
    """封装后的 GraphQL 请求"""
    if config["login"]["token"] == '':
        click.echo("You Need Login First, Run `grank login`")
        exit()
    token = config["login"]["token"]
    headers = {"Authorization": "Bearer %s" % token}
    response = requests.post(
        'https://api.github.com/graphql', json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            response.status_code, query))


def check_exist():
    """检测所需文件是否存在"""
    if not os.path.exists('result'):
        os.makedirs('result')
    if not os.path.exists('output'):
        os.makedirs('output')
    if os.path.isfile('grank.ini'):
        return True
    else:
        return False


def get_config():
    """读取配置文件并返回对应实例"""
    configInstance = configparser.ConfigParser()
    if not check_exist():
        configInstance = get_config_instance()
        with open('grank.ini', 'w') as configfile:
            configInstance.write(configfile)
    configInstance.read('grank.ini')
    return configInstance
    pass

def get_config_instance(token=None, rule=None, start=None, stop=None, top=None, askrule=None):
    configInstance = configparser.ConfigParser()
    configInstance["login"] = {}
    configInstance["login"]["token"] = token if token is not None else ''
    configInstance["social"] = {}
    configInstance["social"]["askrule"] = askrule if askrule is not None else '1'
    configInstance["social"]["rule"] = rule if rule is not None else 'corp|inc'
    configInstance["time"] = {}
    configInstance["time"]["start_time"] = start if start is not None else '2017-01-01'
    configInstance["time"]["end_time"] = stop if stop is not None else datetime.date.today().strftime(
            '%Y-%m-%d')  # 使用今天的日期
    configInstance["rank"] = {}
    configInstance["rank"]["top"] = top if top is not None else '3'# 默认制作前三名的综合图像
    return configInstance
    pass

def set_user_token(token):
    """向配置文件写入用户 Token"""
    config = get_config()
    config["login"]["token"] = token
    with open('grank.ini', 'w') as configfile:
        config.write(configfile)


def set_keyword(rule):
    """向配置文件写入关键词"""
    config = get_config()
    config["social"]["rule"] = rule
    with open('grank.ini', 'w') as configfile:
        config.write(configfile)


def has_next_page(result, mode):
    """判断是否有下一页"""
    if mode == "pr":
        if (has_result(result, "pr")):
            if result["data"]["repository"]["pullRequests"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False

    if mode == "commit":
        if (has_result(result, "commit")):
            if result["data"]["repository"]["ref"]['target']["history"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False
    if mode == "repository":
        if (has_result(result, "repository")):
            if result["data"]["organization"]["repositories"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False

    if mode == "user_repository":
        if (has_result(result, "user_repository")):
            if result["data"]["user"]["repositories"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False


def get_page_cursor(result, mode):
    """判断是否有对应的结果"""
    if mode == "pr":
        return result["data"]["repository"]["pullRequests"]["pageInfo"]["endCursor"]

    if mode == "commit":
        return result["data"]["repository"]["ref"]['target']["history"]["pageInfo"]["endCursor"]

    if mode == "repository":
        return result["data"]["organization"]["repositories"]["pageInfo"]["endCursor"]

    if mode == "user_repository":
        return result["data"]["user"]["repositories"]["pageInfo"]["endCursor"]


def has_result(result, mode):
    """判断是否有对应的结果"""
    if mode == "pr":
        if ("pullRequests" in result["data"]["repository"]):
            if (result["data"]["repository"]["pullRequests"] != None):
                return True
            else:
                return False
        else:
            return False
    elif mode == "commit":
        if ("ref" in result["data"]["repository"]):
            if (result["data"]["repository"]["ref"] != None):
                return True
            else:
                return False
        else:
            return False

    elif mode == 'repository':
        if ("repositories" in result["data"]["organization"]):
            if (result["data"]["organization"]["repositories"] != None):
                return True
            else:
                return False
        else:
            return False
    elif mode == 'user_repository':
        if ("repositories" in result["data"]["user"]):
            if (result["data"]["user"]["repositories"] != None):
                return True
            else:
                return False
        else:
            return False


def cover_time(time):
    """时间的简化处理"""
    if time:
        return time[0:10]
    else:
        return "未标注时间"


def add_item_to_commit_array(item, blank_array):
    """针对 commit 的数组处理"""
    blank_array.append({
        'author': item["node"]["author"]["email"],
        'domain': detect_email_domain(item["node"]["author"]["email"]),
        'is_corp': False,
        'date': cover_time(item["node"]["pushedDate"]),
        "times": 1
    })


def add_item_to_pr_array(item, blank_array):
    """针对 pull requests 的数组处理"""
    blank_array.append({
        "date": cover_time(item["publishedAt"]),
        "times": 1
    })


def export_csv(series, part, owner, repository):
    """导出 Csv 文件"""
    #click.echo("导出 output/" + part + "/" + owner + "/" + "%s.csv" % repository)
    if not os.path.exists('output/' + part + '/' + owner):
        os.makedirs('output/' + part + '/' + owner)
    series.to_csv("output/" + part + "/" + owner + "/" + "%s.csv" % repository)


def export_pickle(df, part, owner, repository):
    """将数据保存到 pickle 中"""
    #click.echo("导出 output/" + part + "/" + owner + "/" + "%s.pkl" % repository)
    if not os.path.exists('output/' + part + '/' + owner):
        os.makedirs('output/' + part + '/' + owner)
    df.to_pickle("output/" + part + "/" + owner + "/" + "%s.pkl" % repository)

def get_activity_average_instance():
    """获取平均值 DF 实例"""
    if not os.path.isfile("output/activity_average.pkl"):
        pd.DataFrame(data={'repos': [], 'score': []}).to_pickle(
            "output/activity_average.pkl")
    return pd.read_pickle("output/activity_average.pkl")


def get_social_average_instance():
    """获取活跃度平均值 DF 实例"""
    if not os.path.isfile("output/social_average.pkl"):
        pd.DataFrame(data={'repos': [], 'score': []}).to_pickle(
            "output/social_average.pkl")
    return pd.read_pickle("output/social_average.pkl")


def set_activity_average(instance, owner, repository, score):
    """保存中间值，并更新 csv 文件"""
    instance = instance.append(pd.Series(
        {"owner": owner, "repos": repository, "score": score}), ignore_index=True)
    instance = instance.drop_duplicates(
        subset=["owner", "repos"]).sort_values(["score"], ascending=False)
    instance.to_pickle("output/activity_average.pkl")
    instance.to_csv("result/activity_rank.csv",float_format="%.2f")


def set_social_average(instance, owner, repository, score):
    """保存中间值，并更新 csv 文件"""

    instance = instance.append(pd.Series(
        {"owner": owner, "repos": repository, "score": score}), ignore_index=True)
    instance = instance.drop_duplicates(
        subset=["owner", "repos"]).sort_values(["score"], ascending=False)

    instance.to_pickle("output/social_average.pkl")
    instance.to_csv("result/social_rank.csv",float_format="%.2f")

def comsum_owner(owner, config):
    click.echo("生成 %s 汇总数据" % owner)
    start_time = config['time']['start_time']
    end_time = config['time']['end_time']

    activity_df = pd.DataFrame({},index=pd.date_range(start=start_time, end=end_time, freq="W"))
    social_df = pd.DataFrame({},index=pd.date_range(start=start_time, end=end_time, freq="W"))

    list = os.listdir('output/activity/' + owner)
    for i in range(0,len(list)):
        path = os.path.join('output/activity/' + owner,list[i])
        if os.path.isfile(path) and os.path.splitext(list[i])[1] == '.pkl' and list[i] != '-ALL-.pkl':
            activity_df = activity_df.add(pd.read_pickle("output/activity/%s/%s" % (owner,list[i])),fill_value = 0)

    activity_df["score"] = activity_df.apply(lambda row: math.sqrt(row.pr*row.pr + row.contributor * row.contributor + row.commit*row.commit), axis=1)
    export_csv(activity_df, 'activity', owner, '-ALL-')
    export_pickle(activity_df, 'activity', owner, '-ALL-')

    list = os.listdir('output/social/' + owner)
    for i in range(0,len(list)):
        path = os.path.join('output/social/' + owner,list[i])
        if os.path.isfile(path) and os.path.splitext(list[i])[1] == '.pkl' and list[i] != '-ALL-.pkl':
            social_df = social_df.add(pd.read_pickle("output/social/%s/%s" % (owner,list[i])),fill_value = 0)

    social_df["score"] = social_df.apply(lambda row: row.community_member / row.all_member, axis=1)

    export_csv(social_df, 'social', owner, '-ALL-')
    export_pickle(social_df, 'social', owner, '-ALL-')

def generate_owner_fig(owner, config):
    click.echo("生成 %s 汇总图表" % owner)
    generate_repository_fig(owner, '-ALL-', config)

def generate_top_fig(config):
    """生成平均值的折线图"""
    #click.echo("生成 TOP 图表")
    start_time = config['time']['start_time']
    end_time = config['time']['end_time']
    top_number = int(config['rank']['top'])

    df = pd.read_pickle("output/activity_average.pkl")
    activity_df = pd.DataFrame(data=[], index=pd.date_range(
        start=start_time, end=end_time, freq="W"))
    social_df = pd.DataFrame(data=[], index=pd.date_range(
        start=start_time, end=end_time, freq="W"))

    for index, row in df.iterrows():
        if len(activity_df.columns) < top_number:
            if not os.path.exists("output/activity/%s/%s.pkl" % (row["owner"],row["repos"])) or not os.path.exists("output/social/%s/%s.pkl" % (row["owner"],row["repos"])):
                continue
            activity_df[row["owner"] + "/" + row["repos"]] = pd.read_pickle(
                "output/activity/%s/%s.pkl" % (row["owner"],row["repos"]))["score"]
            """跟随 activity """
            social_df[row["owner"] + "/" + row["repos"]] = pd.read_pickle(
                "output/social/%s/%s.pkl" % (row["owner"],row["repos"]))["score"] * 100
        else:
            break

    activity_fig = activity_df.plot(title='Activity').get_figure()
    activity_fig.savefig("result/activity_line.png")
    plt.close(activity_fig)
    social_fig = social_df.plot(title='Social').get_figure()
    social_fig.savefig("result/social_line.png")
    plt.close(social_fig)

def generate_repository_fig(owner, repository, config):
    #click.echo("生成 %s/%s 图表" % (owner,repository))
    start_time = config['time']['start_time']
    end_time = config['time']['end_time']
    df = pd.read_pickle("output/activity_average.pkl")
    all_df = pd.DataFrame(data=[], index=pd.date_range(
        start=start_time, end=end_time, freq="W"))

    if not os.path.exists("output/activity/%s/%s.pkl" % (owner,repository)) or not os.path.exists("output/social/%s/%s.pkl" % (owner,repository)):
        click.echo("cant read pkl")
        return False

    all_df['activity'] = pd.read_pickle(
        "output/activity/%s/%s.pkl" % (owner,repository))["score"]
    all_df['social'] = pd.read_pickle(
        "output/social/%s/%s.pkl" % (owner,repository))["score"] * 100

    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_title(owner + "/" + repository)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('activity(%.2f)' % all_df['activity'].mean(), color=color)
    ax1.plot(all_df['activity'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('social(%.2f%%)' % all_df['social'].mean(), color=color)
    ax2.plot(all_df['social'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout()

    if not os.path.exists('result/' + owner):
        os.makedirs('result/' + owner)
    fig.savefig("result/" + owner + "/" + repository + ".png")
    plt.close(fig)

def clean_directory():
    """清空临时目录及结果目录"""
    dirs = ['result','output']
    delete = []
    feature = ['.png','.csv','.pkl']
    exist = False
    for dir in dirs:
        if not os.path.exists(dir):
            continue
        for dirpath,dirnames,filenames in os.walk(dir):
            for file in filenames:
                if os.path.splitext(file)[1] in feature:
                    delete.append(dirpath + '/' + file)
                    click.echo(dirpath+'/'+file)
                    exist = True
    if not exist:
    	click.echo("Workspace is empty now!")
    else:
        confirm = input("\ndelete these files?(yes/no)\n")
        if confirm in ['yes','y','Yes','Y'] :
            for file in delete:
                os.remove(file)
            for dir in dirs:
                if not os.listdir(dir):
                    os.rmdir(dir)
            click.echo("done!")
    pass


def is_corp(email, config):
    """判断是否是企业用户"""
    if re.search(config["social"]["rule"],email) :
        return True
    else:
        return False

def get_user_type(name):
    """判断用户或组织"""
    r = requests.get("https://api.github.com/users/"+name)
    return r.json()["type"] == "User"

def detect_email_domain(name):
    rule = '@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?'
    search_result= re.search(rule,name)

    if search_result == None:
        return ''
    else:
        return search_result.group(0)

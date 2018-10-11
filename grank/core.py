import click
import pandas as pd
import numpy as np
import math
import os
import sys
import warnings

warnings.filterwarnings('ignore')

if sys.version_info[0] != 3:
    """设置 Python 3 的判断如果不是 Python 3 则退出"""
    print("This script requires Python 3")
    exit()

from .libs import helpers
from .libs import query
from .script import activity, crawler, social


@click.group()
def main():
    """Grank Command"""
    pass


@main.command()
@click.option('--rule', prompt=True, help="Regex Rule")
def config(rule):
    """ Config Grank"""
    helpers.set_keyword(rule)
    click.echo('Update Grank.ini Success!')
    pass


@main.command()
@click.option('--token', prompt='Your Personal Access Token',
              help='Generate at https://github.com/settings/tokens')
def login(token):
    """Login with Personal Access Token"""
    helpers.set_user_token(token)
    click.echo('Login Success!')
    pass


@main.command()
def checklogin():
    """ Check User Login"""
    config = helpers.get_config()
    result = helpers.query(query.login_query, config)
    click.echo('Your Username is %s' % result["data"]["viewer"]["login"])
    pass

@main.command()
@click.argument('args', nargs=-1)
def analy(args):
    """Analyse a Github User or Organization"""
    config = helpers.get_config()
    if len(args) == 0:
        click.echo('grank analy owner [repo]')
        return False
    elif len(args) == 1:
        owner = args[0]
        activity_df = pd.DataFrame({},index=pd.date_range(start=start_time, end=end_time, freq="W"))
        social_df = pd.DataFrame({},index=pd.date_range(start=start_time, end=end_time, freq="W"))
        if helpers.get_user_type(owner) is True:
            repository_array = crawler.fetch_user_data(owner, config)
        else:
            repository_array = crawler.fetch_organ_data(owner, config)
        for item in repository_array["repositoryArray"]:
            if os.path.exists('output/activity/' + item["owner"] + '/' + item["repository"] + ".csv"):
                activity_df = activity_df.add(pd.read_pickle("output/activity/%s/%s.pkl" % (item["owner"],item["repository"])),fill_value = 0)
                social_df = social_df.add(pd.read_pickle("output/social/%s/%s.pkl" % (item["owner"],item["repository"])),fill_value = 0)
                continue
                
            data = crawler.fetch_repo_data(item["owner"], item["repository"], config)
            activity_df = activity_df.add(activity.analyse_repo(item["owner"], item["repository"], data, config),fill_value = 0)
            social.analyse_email(data,config)
            social_df = social_df.add(social.analyse_repo(item["owner"], item["repository"], data, config),fill_value = 0)
            
            # 生成折线图
            helpers.generate_repository_fig(config, item['owner'], item['repository'])

        activity_df["score"] = activity_df.apply(lambda row: math.sqrt(row.pr*row.pr + row.contributor * row.contributor + row.commit*row.commit), axis=1)
        social_df["score"] = social_df.apply(lambda row: row.community_member / row.all_member, axis=1)
        
        helpers.export_csv(activity_df, 'activity', owner, '-ALL-')
        helpers.export_csv(social_df, 'social', owner, '-ALL-')
        helpers.export_pickle(activity_df, 'activity', owner, '-ALL-')
        helpers.export_pickle(social_df, 'social', owner, '-ALL-')
        helpers.generate_repository_fig(config, owner, '-ALL-')
    else:
        owner = args[0]
        repo = args[1]
        data = crawler.fetch_repo_data(owner, repo, config)
        activity.analyse_repo(owner, repo, data, config)
        social.analyse_email(data,config)
        social.analyse_repo(owner, repo, data, config)
        helpers.generate_repository_fig(config, owner, repo)
        
    helpers.generate_top_fig(config)        
    pass

@main.command()
def clean():
    """Delete UnUsed File"""
    helpers.clean_directory()
    pass


if __name__ == '__main__':
    main()

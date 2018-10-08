import click
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
@click.argument('organization')
@click.argument('repo')
def repo(organization, repo):
    """Analyse a Github Repository"""
    config = helpers.get_config()
    data = crawler.fetch_repo_data(organization, repo, config)
    activity.analyse_repo(organization, repo, data, config)
    social.analyse_email(data,config)
    social.analyse_repo(organization, repo, data, config)
    pass

@main.command()
@click.argument('name')
def analy(name):
    """Analyse a Github User or Organization"""
    config = helpers.get_config()
    if helpers.get_user_type(name) is True:
        repository_array = crawler.fetch_user_data(name, config)
    else:
        repository_array = crawler.fetch_organ_data(name, config)
    for item in repository_array["repositoryArray"]:
        data = crawler.fetch_repo_data(
            item["owner"], item["repository"], config)
        activity.analyse_repo(item["owner"], item["repository"], data, config)
        social.analyse_email(data,config)
        social.analyse_repo(item["owner"], item["repository"], data, config)
    pass

@main.command()
def clean():
    """Delete UnUsed File"""
    helpers.clean_directory()
    pass


if __name__ == '__main__':
    main()

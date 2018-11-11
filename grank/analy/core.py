__all__ = ['get_analy']

def get_analy(token=None,start=None,stop=None,owner=None,repo=None):
    from ..script.crawler import fetch_repo_data
    from ..libs.helpers import get_config_instance
    from ..script.activity import analyse_repo
    from ..script.social import analyse_repo as analyse_social
    if owner is None:
        raise ValueError('owner invalid!')
    if repo is None:
        raise ValueError('repo invalid!')
    config = get_config_instance(token=token,start=start,stop=stop)
    data = fetch_repo_data(owner,repo,config)
    activity = analyse_repo(owner, repo, data, config, ret_score = True)
    social = analyse_social(owner, repo, data, config, ret_score = True)
    return {'activity': activity, 'social':social}

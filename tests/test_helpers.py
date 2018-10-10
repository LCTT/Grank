from grank.libs import helpers
import configparser
def test_detect_email_domain():
    gmail_domain = helpers.detect_email_domain('test_case@gmail.com')
    assert gmail_domain == '@gmail.com'

    localhost_domain = helpers.detect_email_domain('localhost')
    assert localhost_domain == ''

def test_get_user_type():
    test_user = helpers.get_user_type('bestony')
    assert test_user == True
    test_organ = helpers.get_user_type('lctt')
    assert test_organ == False

def test_is_corp():
    configInstance = configparser.ConfigParser()
    configInstance["social"] = {}
    configInstance["social"]["rule"] = 'linux.cn'
    test_public_mail = helpers.is_corp('xiqingongzi@gmail.com',configInstance)
    test_corp_mail = helpers.is_corp('bestony@linux.cn',configInstance)
    assert test_public_mail == False
    assert test_corp_mail == True

def test_cover_time():
    real_time = helpers.cover_time('2016-12-29T15:46:23Z')
    none_time = helpers.cover_time(None)
    blank_time = helpers.cover_time('')
    assert real_time == '2016-12-29'
    assert none_time == '未标注时间'
    assert blank_time == '未标注时间'

def test_has_result_success():
    test_ok_result = {"data":{"repository":{"name":"example","pullRequests":{"pageInfo":{"endCursor":"Y3Vyc29yOnYyOpHOBfDVGg==","hasNextPage":True},"nodes":[{"publishedAt":"2016-12-29T15:46:23Z","id":"MDExOlB1bGxSZXF1ZXN0OTk2NjkyNzQ="}]},"ref":{"target":{"history":{"pageInfo":{"endCursor":"56f531de853c2bbd974e6612c8d4cd1ab59f169a 0","hasNextPage":True},"totalCount":217,"edges":[{"node":{"author":{"email":"example"},"pushedDate":"2018-08-22T06:56:48Z"}}]}}}}}}
    test_user_result = {"data":{"user":{"repositories":{"pageInfo":{"hasPreviousPage":True,"startCursor":"Y3Vyc29yOnYyOpHOCPih1A=="},"nodes":[{"name":"sspai-cse"}]}}}}
    test_organ_result = {"data":{"organization":{"repositories":{"pageInfo":{"hasPreviousPage":True,"startCursor":"MTg="},"nodes":[{"name":"Grank"}]}}}}
    test_has_pr = helpers.has_result(test_ok_result,'pr')
    test_has_commit = helpers.has_result(test_ok_result,'commit')
    test_user_repository = helpers.has_result(test_user_result,'user_repository')
    test_organ_repository = helpers.has_result(test_organ_result,'repository')
    assert test_has_pr == True
    assert test_has_commit == True
    assert test_user_repository == True
    assert test_organ_repository == True

def test_has_result_fail():
    test_none_result = {"data":{"repository":{"name":"example","pullRequests":None,"ref":None}}}
    test_user_none_result = {"data":{"user":{"repositories":None}}}
    test_organ_none_result = {"data":{"organization":{"repositories":None}}}

    test_none_has_pr = helpers.has_result(test_none_result,'pr')
    test_none_has_commit = helpers.has_result(test_none_result,'commit')
    test_none_user_repository = helpers.has_result(test_user_none_result,'user_repository')
    test_none_organ_repository = helpers.has_result(test_organ_none_result,'repository')

    assert test_none_has_pr == False
    assert test_none_has_commit == False
    assert test_none_user_repository == False
    assert test_none_organ_repository == False

def test_has_result_blank():
    test_blank_result = {"data":{"repository":{"name":"example"}}}
    test_blank_user_result = {"data":{"user":{"name":"example"}}}
    test_blank_organ_result = {"data":{"organization":{"name":"example"}}}

    test_blank_pr = helpers.has_result(test_blank_result,'pr')
    test_blank_commit = helpers.has_result(test_blank_result,'commit')
    test_blank_user = helpers.has_result(test_blank_user_result,'user_repository')
    test_blank_organ = helpers.has_result(test_blank_organ_result,'repository')

    assert test_blank_pr == False
    assert test_blank_commit == False
    assert test_blank_user == False
    assert test_blank_organ == False

def test_get_page_cursor():
    test_organ_result = {"data":{"organization":{"repositories":{"pageInfo":{"endCursor":"123"}}}}}
    test_user_result = {"data":{"user":{"repositories":{"pageInfo":{"endCursor":"123"}}}}}
    test_repo_result = {"data":{"repository":{"name":"Example","pullRequests":{"pageInfo":{"endCursor":"123"}},"ref":{"target":{"history":{"pageInfo":{"endCursor":"123"}}}}}}}

    test_commit_page = helpers.get_page_cursor(test_repo_result,'commit')
    test_pr_page = helpers.get_page_cursor(test_repo_result,'pr')
    test_organ_page = helpers.get_page_cursor(test_organ_result,'repository')
    test_user_page = helpers.get_page_cursor(test_user_result,'user_repository')

    assert test_commit_page == '123'
    assert test_pr_page == '123'
    assert test_organ_page == '123'
    assert test_user_page == '123'

def test_has_next_page_success():
    test_repo_result = {"data":{"repository":{"pullRequests":{"pageInfo":{"hasNextPage":True}},"ref":{"target":{"history":{"pageInfo":{"hasNextPage":True}}}}}}}
    test_user_result = {"data":{"user":{"repositories":{"pageInfo":{"hasNextPage":True}}}}}
    test_organ_result = {"data":{"organization":{"repositories":{"pageInfo":{"hasNextPage":True}}}}}

    test_commit_next = helpers.has_next_page(test_repo_result,'commit')
    test_pr_next = helpers.has_next_page(test_repo_result,'pr')
    test_user_next = helpers.has_next_page(test_user_result,'user_repository')
    test_organ_next = helpers.has_next_page(test_organ_result,'repository')

    assert test_commit_next == True
    assert test_pr_next == True
    assert test_organ_next == True
    assert test_user_next == True

def test_has_next_page_fail():
    test_repo_result = {"data":{"repository":{"pullRequests":{"pageInfo":{"hasNextPage":False}},"ref":{"target":{"history":{"pageInfo":{"hasNextPage":False}}}}}}}
    test_user_result = {"data":{"user":{"repositories":{"pageInfo":{"hasNextPage":False}}}}}
    test_organ_result = {"data":{"organization":{"repositories":{"pageInfo":{"hasNextPage":False}}}}}

    test_commit_next = helpers.has_next_page(test_repo_result,'commit')
    test_pr_next = helpers.has_next_page(test_repo_result,'pr')
    test_user_next = helpers.has_next_page(test_user_result,'user_repository')
    test_organ_next = helpers.has_next_page(test_organ_result,'repository')

    assert test_commit_next == False
    assert test_pr_next == False
    assert test_organ_next == False
    assert test_user_next == False

def test_get_config():
    configInstance = helpers.get_config()
    assert type(configparser.ConfigParser()) == type(configInstance)


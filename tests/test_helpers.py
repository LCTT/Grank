from grank.libs import helpers
def test_detect_email_domain():
    gmail_domain = helpers.detect_email_domain('test_case@gmail.com')
    assert gmail_domain == '@gmail.com'

    localhost_domain = helpers.detect_email_domain('localhost')
    assert localhost_domain == ''

def test_get_user_type():
    test_user = helpers.get_user_type('bestony')
    assert test_user == True
    test_ogran = helpers.get_user_type('lctt')
    assert test_ogran == False
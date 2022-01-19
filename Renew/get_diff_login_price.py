import json
import pytest
import requests
from tool import get_diff_login as gdl


# 未登录的时候
# admin/cw/内部账号登录
# 卡号持有者上级登录/有差价/无差价
# 卡号持有者登录
# 区别是token

# 未登录的价格/与持有卡号人价格一致
def test_no_login():
    re = requests.post(url=gdl.url, data=json.dumps(gdl.data)).json()
    allRenewPrice = re['data']['allRenewPrice']
    print(allRenewPrice)
    assert allRenewPrice == 24.0 + 0.1


# admin/内部账号登录
def test_admin_login():
    headers = {
        'token': gdl.token_admin
    }
    re = requests.post(url=gdl.url, data=json.dumps(gdl.data), headers=headers)
    allRenewPrice = re.json()['data']['allRenewPrice']
    print(allRenewPrice)
    assert allRenewPrice == 2.0
    print('admin价格获取成功')


# 持卡人上级的价格
def test_card_holder_superior_login():
    headers = {
        'token': gdl.token_sangjy
    }
    re = requests.post(url=gdl.url, data=json.dumps(gdl.data), headers=headers)
    allRenewPrice = re.json()['data']['allRenewPrice']
    print(allRenewPrice)
    assert allRenewPrice == 23.0 + 0.1
    print('上级持有者价格正确')


# 持卡人的价格
def test_card_holder_login():
    Headers = {
        'token': gdl.token_test13
    }
    re = requests.post(url=gdl.url, data=json.dumps(gdl.data), headers=Headers)
    print(re.text)
    allRenewPrice = re.json()['data']['allRenewPrice']
    print(allRenewPrice)
    assert allRenewPrice == 24.0 + 0.1
    print('holder通过')


if __name__ == '__main__':
    pytest.main("-vs", "get_diff_login_price.py")


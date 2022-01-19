import json
import requests
from others import login
import pytest

url = 'http://prerelease.simcards.cn/card/batchSell.do'

Headers = {
    'content-type': 'application/json',
    'token': login.token
}


# 卡号销售
def test_batch_card_no():
    data = {
        "cardNo": [
            "1440408990769",
            "14646445464"
        ],
        "userId": 20997
    }
    re = requests.put(url=url, data=json.dumps(data), headers=Headers)
    assert re.json()["ret"] == 1
    print("销售成功")


# icc_id销售
def test_batch_icc_id():
    data = {
        "cardNo": [
            "1440408990769",
            "14646445464"
        ],
        "userId": 20997
    }
    re = requests.put(url=url, data=json.dumps(data), headers=Headers).json()
    assert re.json()["ret"] == 1
    print("销售成功")


# 销售卡号+icc_id
def test_card_no_and_icc_id():
    data = {
        "cardNos": [
            "1440408990819",
            "1440408990505",
            "89860440191890110000",
            "89860435191842032813",
            "89860405191841323755"
        ],
        "userId": 16396
    }
    re = requests.put(url=url, data=json.dumps(data), headers=Headers)
    assert re.json()["ret"] == 1
    print("销售成功")


# 卡号存在流量池
def test_batch_flow_pool():
    data = {
        "cardNo": [
            "1440408990769",
            "14646445464"
        ],
        "userId": 7
    }
    re = requests.put(url=url, data=json.dumps(data), headers=Headers)
    assert re.json()["ret"] == 1
    print("销售成功")


if __name__ == '__main__':
    pytest.main("-s", "batchSell2.py")

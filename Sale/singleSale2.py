import json
import requests
import Sell
import pytest


# 卡号销售
def test_card_no():
    data = {
        "cardNo": "1440408990769",
        "userId": 20997,
        "remarks": "123"
    }
    re = requests.put(url=Sell.url, data=json.dumps(data), headers=Sell.Headers)
    assert re.json()["ret"] == 1
    print('销售成功')


# icc_id销售
def test_icc_id():

    data = {
        "cardNo": "898604401918C0690768",
        "userId": 20997,
        "remarks": "123"
    }
    re = requests.put(url=Sell.url, data=json.dumps(data), headers=Sell.Headers)
    assert re.json()["ret"] == 1
    print('icc_id用例通过')


# 卡号存在流量池
def test_flow_pool():
    data = {
        "cardNo": "1440426774448",
        "userId": 7,
        "remarks": "123"
    }
    re = requests.put(url=Sell.url, data=json.dumps(data), headers=Sell.Headers)
    print(re.text)
    assert re.json()["ret"] == 1
    print('流量池卡号用例通过')


if __name__ == '__main__':
    pytest.main("-s", "singleSale2.py::test_icc_id")

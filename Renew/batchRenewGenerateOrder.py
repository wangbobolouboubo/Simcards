# 二维码接口调起(创建订单)
import json
import requests
from others import login

url = 'http://prerelease.simcards.cn/recharge/batchRenewGenerateOrder.do'
headers = {
    'context-type': 'application/json',
    'token': login.token
}

data = {
    "cardNos": [
        # # //月卡
        # // "1440408990831",
        # // "1440408990824"
        # "1440420690855",
        "17242523444"
    ],
    # // 月续费
    "renewMonth": "1",
    # //* 年续费
    "renewYear": "1",
    # // 续费类别（0表示按月续费  1表示按年续费）
    "renewType": "0",
    # //支付方式, 0: 支付宝 , 1: 微信  , 2: 余额
    "rechargeType": "0"
}

re = requests.post(url=url, data=json.dumps(data), headers=headers)
print(re.text)


# 该接口只是创建订单 只是生成的订单--在充值记录中显示--但是并不会延长卡号的到期时间、减少余额、产生差价
# 注意维护数据：test13,17242523444,续费一个月


# 余额-单卡-月卡
def test_balance_month_card():
    pass


# 余额-单卡-年卡
def test_balance_year_card():
    pass


# 余额-多卡-月卡-同套餐
def test_balance_batch_month_card_same_pack():
    pass


# 余额-多卡-年卡-同套餐
def test_balance_batch_year_card_same_pack():
    pass


# 余额-多卡-月卡-不同套餐
def test_balance_batch_month_card_diff_pack():
    pass


# 余额-多卡-年卡-不同套餐
def test_balance_batch_year_card_diff_pack():
    pass


# 余额-多卡-年卡-月卡-混合-充值月
def test_balance_batch_year_month_month():
    pass


# 余额-多卡-年卡-月卡-混合-充年
def test_balance_batch_year_month_month():
    pass


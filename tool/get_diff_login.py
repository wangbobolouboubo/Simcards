import requests

url = 'http://prerelease.simcards.cn/recharge/batchRenewPrice.do'

data = {
    "cardNos": [
        "17242523444"
    ],
    # // 月续费 1是续费一个月，2是续费两个月，以此类推
    "renewMonth": "1",
    # //* 年续费
    "renewYear": "1",
    # // 续费类别（0表示按月续费  1表示按年续费）
    "renewType": "1",
    # //支付方式, 0: 支付宝 , 1: 微信  , 2: 余额
    "rechargeType": "2"
}
# admin 登录
req = requests.get(
    'http://prerelease.simcards.cn/user/login.do?loginName=admin&passWord=seeworld121&lang=zh-CN)').json()
token_admin = req['data']['token']

# sangjy 登录
req = requests.get(
    'http://prerelease.simcards.cn/user/login.do?loginName=sangjy&passWord=123456&lang=zh-CN)').json()
token_sangjy = req['data']['token']

# test13
req = requests.get(
    'http://prerelease.simcards.cn/user/login.do?loginName=test13&passWord=123456&lang=zh-CN)').json()
token_test13 = req['data']['token']

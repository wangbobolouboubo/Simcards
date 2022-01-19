# 登录接口拿token
import requests
req = requests.get('http://prerelease.simcards.cn/user/login.do?loginName=test13&passWord=123456&lang=zh-CN').json()
token = req['data']['token']
print(token)

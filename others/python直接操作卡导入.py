import requests

# # 上传的excel
# file
# # 套餐Id
# packId
# # 用户Id
# userId
# # 卡类型, 公司类型
# cardType
# # APN类型 0:CMMTM;1:CMIOT;
# apnType
# # 卡形态：0非贴片卡，1贴片卡
# cardForm
# # 备注
# remark

# 登录接口拿token
req = requests.get('http://prerelease.simcards.cn/user/login.do?loginName=admin&passWord=seeworld121&lang=zh-CN').json()
token = req['data']['token']
print(token)

request_url = 'http://prerelease.simcards.cn/card/import.do'
request_data = {
    'packId': 200,
    'userId': 21007,
    'cardType': 8,
    'apnType': 0,
    'apnType': 0,
    'remark': '导入'
}
# request_file = {'testfile': (('testfile', open('D:/testfile/导入2.xlsx','rb')))}
request_files = {'file': open('D:/testfile/导入2.xlsx', 'rb')}
headers = {
    'Content-Type': 'multipart/form-data',
    'token': token
}
req = requests.post(url=request_url, data=request_data, files=request_files, headers=headers)
print(req.text)
print(req.status_code)


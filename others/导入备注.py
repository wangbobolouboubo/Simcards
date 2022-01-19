from requests_toolbelt import MultipartEncoder
import requests

req = requests.get('http://prerelease.simcards.cn/user/login.do?loginName=admin&passWord=seeworld121&lang=zh-CN').json()
token = req['data']['token']
print(token)


update_url = 'http://prerelease.simcards.cn/card/importRemarks.do'

data = MultipartEncoder(fields={'propertyMessageXml': ('filename', open('D:/Desktop/importRemarks.xlsx', 'rb'))})
print(update_url)
headers = {
    'Content-Type': 'multipart/form-data',
    'token': token
}
req = requests.post(url=update_url, data=data, headers=headers)
print(req.status_code)
print(req.json())
print(12)



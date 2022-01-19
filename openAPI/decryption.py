import requests
from openAPI.SingleCardInformationQuery import re

url = 'http://prerelease.simcards.cn/OpenApi/crypt.do'

data = {
    "request": re.json()['data'],
    "crypt": "0",
    "secretKey": "f6a9af4e",
    "iv": "54b2d34e"
}

req = requests.post(url=url, data=data)
print(req.text)
print(req.json())

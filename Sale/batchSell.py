
import json
import requests
from others import login

url = 'http://prerelease.simcards.cn/card/batchSell.do'

data = {
    "cardNos": [
        "898604401918C0690769",
        "898604351918C1262818",
        "898604351918C1262817",
        "898604351918C1262816",
        "898604351918C1262815"
    ],
    "userId": 19904
}

Headers = {
    'content-type': 'application/json',
    'token': login.token
}

re = requests.put(url=url, data=json.dumps(data), headers=Headers)
print(re.json())
print(re.text)

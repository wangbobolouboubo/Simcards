
import json
import requests
from others import login

url = 'http://prerelease.simcards.cn//card/singleSell.do'
data = {
    "cardNo": "1440408990769",
    "userId": 7,
    "remarks": "123"
}
Headers = {
    'content-type': 'application/json',
    'token': login.token
}


re = requests.put(url=url, data=json.dumps(data), headers=Headers)
print(re.text)
print(re.json()["ret"])
assert re.json()["ret"] == 1
print('恭喜')



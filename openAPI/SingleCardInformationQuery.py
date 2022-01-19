import json
import requests

url = 'http://prerelease.simcards.cn/OpenApi/Router'
data = {
    "Parameter": "uek75A4eejMpkjKjjIP/NewuG9a4kOsxa+UBKo82GLZ4CZOnSs1eLoz4a3DDVV8MQiNYjMwBKoo=",
    "Method": "QueryCard",
    "platformId": "f6a9af4e7ff24399a95b4f2310462c66"
}
re = requests.post(url=url, data=json.dumps(data))
print(re.text)
print(re.json()['data'])



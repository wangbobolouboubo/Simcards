#
# cardNo = "1440408990769"
# cardNos = [
#     "",
#     "",
#     "",
#     ""
# ]
# userId = 16396
# remarks = "销售备注"
#
from others import login

url = 'http://prerelease.simcards.cn//card/singleSell.do'

Headers = {
    'content-type': 'application/json',
    'token': login.token
}

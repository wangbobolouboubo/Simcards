# url        ：http://prerelease.simcards.cn//card/singleSell.do
# method     ：
# 格式        ：JSON
# 请求方式     ：put
# 请求参数     ：cardNo 卡号 必填 , userId 销售到的用户Id 必填,  remarks 备注 必填
# 应答参数     : ret  返回结果, 1是成功, 0 是失败, time 服务器时间戳, msg 服务器返回消息
# 请求示例
# {
#     "cardNo":"01010101010101",
#     "userId":"20852",
#     "remarks":"测试单卡销售1"
# }
#



# 返回示例

# {
#     "code": "200",
#     "data": null,
#     "msg": null,
#     "ret": 1,
#     "time": 1608197166086,
#     "total": null
# }

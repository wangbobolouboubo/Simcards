import pymssql  # 引入pymssql模块


def conn():
    connect = pymssql.connect(
        server='39.107.103.34:1433',
        user='sa',
        password='Zxcvbnm*951',
        database='Recharge',  # 建立连接
    )
    if connect:
        print("连接成功!")
    return connect


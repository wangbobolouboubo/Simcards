from consql.connect_sqlserver_s.conn import conn

con = conn()
c1 = con.cursor(as_dict=True)
sql = "select * from users where loginName ='nobug'"
c1.execute(sql)
data = c1.fetchone()
print(data)

c2 = con.cursor(as_dict=True)
sql = "select BalanceAmount from users where loginName ='nobug'"
c2.execute(sql)
data = c1.fetchone()
print(data)

c1.close()  # 关闭游标
c2.close()  # 关闭游标
con.close()  # 关闭连接

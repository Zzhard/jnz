# pip install xpinyin
# import xpinyin
# s = xpinyin.Pinyin()
# pinyin = s.get_pinyin('倪菊芳','')
# print(pinyin)

#1、ip

host='118.24.3.40'
user='jxz'
password='123456' #密码只能是字符串
db='jxz'
port=3306#端口号只能写int类型
charset='utf8'#只能写utf8，不能写utf-8
import pymysql
conn = pymysql.connect(host=host,password=password,
                user=user,db=db,port=port,
                charset=charset,autocommit=True
                )#建立连接

cur= conn.cursor() #建立游标
# cur.execute()#只是帮你执行sql语句
# print(cur.fetchall())#获取数据库里面的所有的结果
# print('fetchone',cur.fetchone())
# sql='insert into app_myuser (username,passwd,is_admin) VALUE ("python123456","123456",1);'
sql='select * from app_myuser limit 5;'
cur.execute(sql)
print(cur.description)#获取这个表里面的所有字段信息
# conn.commit()#提交
cur.close()
conn.close()

def my_db(ip,user,password,db,sql,port=3306,charset='utf8'):
    conn = pymysql.connect(
        host=ip,user=user,password=password,
        db=db,
        port=port,charset=charset,autocommit=True
    )
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

def my_db2(sql):
    conn = pymysql.connect(
        host='118.24.3.40',user='jxz',password='123456',
        db='jxz',
        port=3306,charset='utf8',autocommit=True
    )
    pass


import pymysql
from conf.setting import mysql_info,redis_info
import redis
import jsonpath
class MySQL:
    def __init__(self):
        self.conn = pymysql.connect(**mysql_info)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        #初始化的时候就连接数据库
    def execute_many(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        if res:
            return res
    def execute_one(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        if res:
            return res

    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('连接已经关闭')
import datetime
import os,yagmail
from conf import setting
def get_real_value(key,response):
    #从字典里面获取key对应的value
    res = jsonpath.jsonpath(response,'$..%s'%key)
    #$..%s这个是jsonpath这个模块的用法
    if res:
        return res[0]

def get_redis():
    return redis.Redis(**redis_info)

def make_today_dir():
    #创建当天的文件夹，返回绝对路径
    today = str(datetime.date.today())
    abs_path = os.path.join(setting.REPORT_PATH,today)
    #拼成当天的绝对路径
    if os.path.exists(abs_path):
        pass
    else:
        os.mkdir(abs_path)

    return abs_path

def send_mail(content,file_path=None):
    #发邮件，传入邮件正文和附件
    m = yagmail.SMTP(**setting.MAIL_INFO,)
    subject = '接口测试报告_%s'%str(datetime.datetime.today())
    m.send(subject=subject,to=setting.TO,contents=content,attachments=file_path)


mysql = MySQL()

r = get_redis()
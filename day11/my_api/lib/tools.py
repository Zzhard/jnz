import pymysql
from conf.setting import mysql_info,redis_info
import redis
from hashlib import md5
class MySQL:
    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        self.conn = pymysql.connect(host=host,user=user,password=password,db=db,port=port,charset=charset)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        #初始化的时候就连接数据库
    def execute_many(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()  # [ {},{}  ]
    def execute_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('连接已经关闭')

def my_md5(s):
    m = md5(str(s).encode() )
    return m.hexdigest()

def check_float(s):
    '''
    这个函数的作用就是判断传入的字符串是否是合法的小数
    :param s: 传入一个字符串
    :return: True/false
    '''
    s = str(s)
    if s.count('.')==1:
        s_split = s.split('.')
        left,right = s_split
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left[1:].isdigit() \
            and right.isdigit():
            return True
    return False

def get_redis():
    return redis.Redis(**redis_info)

db=MySQL('118.24.3.40','jxz','123456','jxz')

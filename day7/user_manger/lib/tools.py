

# import pymysql
import redis
from conf import setting
def mydb(sql):
    print('操作数据库')
    # pymysql.coonect(host=setting.mysql_host)
    pass

def my_redis():
    print('操作reids')
    # r = redis.Redis(host=setting.redis_host,password=setting.redis_host)
    pass

def my_md5():
    pass
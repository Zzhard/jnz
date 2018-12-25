import os
BAE_PATH  = os.path.dirname(
os.path.dirname(os.path.abspath(__file__))
) #atp的目录

LOG_PATH = os.path.join(BAE_PATH,'logs') #log目录
CASE_PATH = os.path.join(BAE_PATH,'cases') #case目录
REPORT_PATH = os.path.join(BAE_PATH,'report') #report目录
SQL_PATH = os.path.join(BAE_PATH,'sql_file') #=存放sql的目录
DATA_PATH = os.path.join(BAE_PATH,'data') #存参数化文件的地方


MAIL_INFO = {
    'user':'uitestp4p@163.com',
    'password':'houyafan123',
    'host':'smtp.163.com',
    # 'smtp_ssl':True,#发件箱是qq邮箱的话，改成True
}

TO = ['511402865@qq.com','496647026@qq.com','649623416@qq.com','ray-zuo@qq.com']

HOSTS = {
    'QA':'http://api.nnzhp.cn',#测试环境
    'DEV':'http://dev.nnzhp.cn',#开发环境
    'PRE':'http://pre.nnzhp.cn' #预生产环境
}


mysql_info = {
    'host':'118.24.3.40',
    'port':3306,
    'user':'besttest',
    'password':'HK139bc',
    'db':'main',
    'charset':'utf8',
    'autocommit':True
}
#mysql 配置信息
redis_info = {
    'host': '118.24.3.40',
    'password': 'HK139bc&*',
    'port': 6379,
    'db': 0,
    'decode_responses': True
}



default_host = HOSTS.get('QA')  #默认测试环境的地址
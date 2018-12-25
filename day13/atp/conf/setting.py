import os
BAE_PATH  = os.path.dirname(
os.path.dirname(os.path.abspath(__file__))
) #atp的目录

LOG_PATH = os.path.join(BAE_PATH,'logs') #log目录
CASE_PATH = os.path.join(BAE_PATH,'cases') #case目录
REPORT_PATH = os.path.join(BAE_PATH,'report') #report目录


MAIL_INFO = {
    'user':'xxxx@qq.com',
    'password':'sdfsdf',
    'host':'smtp.qq.com',
    'smtp_ssl':True,#发件箱是qq邮箱的话，改成True
}

TO = ['511402865@qq.com','496647026@qq.com','649623416@qq.com','ray-zuo@qq.com']


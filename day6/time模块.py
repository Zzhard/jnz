#和时间相关的操作

import time

# time.sleep(30)

# 格式化好的时间 20180915 14：08:53

# 时间戳  从计算机诞生那天到现在过了多少秒

# res = time.strftime('%Y-%m-%d %H:%M:%S') #取当前的格式化日期
res = time.time()#获取当前的时间戳

#时间元组

#先把格式化好的时间转成时间元组


#1992-01-02

# time_tuple = time.strptime('2038-08-29 19:23:59','%Y-%m-%d %H:%M:%S')#把格式化好的时间转成时间元组
# print(time.mktime(time_tuple))

def str_to_timestamp(time_str=None,format='%Y%m%d%H%M%S'):
    #格式化好的时间转时间戳的
    #不传参数的话返回当前的时间戳
    if time_str:
        time_tuple = time.strptime(time_str, format)  # 把格式化好的时间转成时间元组
        timestamp = time.mktime(time_tuple)
    else:
        timestamp = time.time()
    return int(timestamp)

# print(str_to_timestamp())
# print(str_to_timestamp('20391123175123'))
# print(str_to_timestamp('2013-08-09','%Y-%m-%d'))


#时间戳转格式化好的时间

#先把时间戳转成时间元组


# res = time.gmtime(time.time())#是把时间戳转时间元组的，标准时区
res = time.localtime(time.time())#是把时间戳转时间元组的，当前时区
res2 = time.strftime('%Y-%m-%d %H:%M:%S',res)
print(res2)
def timestamp_to_strtime(timestamp=None,format='%Y-%m-%d %H:%M:%S'):
    #这个函数是用来把时间戳转成格式化好的时间
    #如果不传时间戳的话，那么就返回当前的时间
    if timestamp:
        time_tuple = time.localtime(timestamp)
        str_time = time.strftime(format,time_tuple)
    else:
        str_time = time.strftime(format)
    return str_time

#用当前的时间戳+50年的秒数，时间戳转成格式化好的时间

five = str_to_timestamp() - (3*24*60*60)
res = timestamp_to_strtime(five)
print('50年后的时间是',res)
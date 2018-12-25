#1、要从日志里面找到1分钟之内访问超过200次的
#2、每分钟都运行一次

# 1、读取文件内容，获取到ip地址
# 2、把每个ip地址存起来 {}
# 3、判断ip访问的次数是否超过200次
# 4、加入黑名单 print

#['118.24.4.30','118.24.4.30','118.24.4.30','118.1xx.x.xx','118.1xx.x.xx']
# {
#     '118.23.3.40':2,
#     '118.23.3.41':5
# }
import time
point = 0 #初始的位置
while True:
    ips = {}
    f = open('access.log',encoding='utf-8')
    f.seek(point)
    for line in f: #循环取文件里面每行数据
        ip = line.split()[0] #按照空格分割，取第一个元素就ip
        if ip in ips:#判断这个ip是否存在
            # ips[ip] = ips[ip]+1
            ips[ip]+=1#如果存在的话，次数加+1
        else:
            ips[ip]=1 #如果不存在ip的次数就是1
    point = f.tell() #记录文件指针位置
    f.close()
    for ip,count in ips.items():#循环这个字典，判断次数大于200的
        if count>=200:
            print('%s 加入黑名单'%ip)
    time.sleep(60)
#point = 789
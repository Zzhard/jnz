def my(name,sex):
    #位置参数，必填
    #默认值参数
     #函数体
    return name

def db_connect(ip,port=3306):
    print(ip,port)

# db_connect('118.24.3.40',3307)
# db_connect('118.24.3.40')
import json
def op_file_tojson(file_name,dic=None):
    if dic:
        with open(file_name,'w',encoding='utf-8') as fw:
            json.dump(dic,fw)
    else:
        f = open(file_name,encoding='utf-8')
        content = f.read()
        if content:
            res = json.loads(content)
        else:
            res = {}
        f.close()
        return res


res = db_connect('118.24.3.40',3307)

def my2():
    for i in range(50):
        return i

def my3():
    a = 1
    b = 2
    c = 3
    return a,b,c

b,c,d = my3()
s = my3()
# print(b,c,d)
# print(s)

# a,b,c = 1,2,3
#
# a = b = c = 1

# def my4(s:str,d:dict):
#     print(s)
#     print(d)
#
# my4(134,'abcd')


#return 有2个作用
#1、结束函数，只要函数里面遇到return，函数立即结束运行
#2、返回函数处理的结果
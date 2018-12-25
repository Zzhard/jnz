import os,glob
# print(os.listdir())
# for f in os.listdir():
#     if f.endswith('.py'):
#         os.remove(f)
# print(glob.glob('*')
# print(d['abc'])
# s='a'
# print(int(s))
# print(10/0)i
# import pymysql
# coon = pymysql.connect(host='118.24.3.40',user='jxz',
#                 password='123456',db='jxz')
# cur= coon.cursor()
# cur.execute('select  from a;')
#
# for i in range(20):
#     print(i)

# try:
#     s = 10/0
# except ZeroDivisionError as e:
# # except ZeroDivisionError, e:  这个是python2里面的写法
#     print('走这里')
#     print(e)

def calc(a,b):
    try:
        res = a/b
    # except ZeroDivisionError as e:
    #     res = '除数不能为零, %s'%e
    # except TypeError as e:
    #     res = '类型错误,只能数字类型 %s'%e
    except Exception as e:
        print(e)
    # return res
# res = calc('k',1) #TypeError
# # calc(10,0)  # ZeroDivisionError
# res = calc(10,0) #TypeError


money = input('enter:')
try:
    money = int(money)
except Exception as e:#产生异常了，走这边
    print('输入金额错误！')
else:#没有出现异常的话就这里
    print(money+1)
finally:
    print('什么时候执行finally')

# sssk
# 689


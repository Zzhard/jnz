# 作业：
#     1、写一个登陆的小程序
#         username = tanailing
#         passwd = 123456
#         1、输入账号密码,输入正确就登陆成功，              username = input('xx')  password = input()
#             提示欢迎xxxx登陆，今天的日期是多少
#         2、最多输入错误3次        循环 for while  循环3次
#             账号/密码错误，请重新登陆      if 条件判断的     1、账号密码正确 2、输入为空、3、账号密码不正确
#         3、如果失败测试超过3次，提示，失败次数过多    else
#         4、要校验输入是否为空，如果输入为空，你要提示账号./密码不能为空
#            什么都不输入和输入一个空格多个空格都算空。
#            输入为空也算操作错误一次

import datetime
# for i in range(3):
#     username = input('请输入你的用户名：').strip()
#     password = input('请输入你的密码：').strip()
#     if username=='tanailing' and password == '123456':
#         print('欢迎%s登陆,今天的日期是%s'%(username,datetime.datetime.today()))
#         break
#     elif username=='' or password =='':
#         print('账号和密码都不能为空！')
#     else:
#         print('账号/密码错误')
# else:
#     print('错误次数过多')


count = 0
while count<3:
    count += 1
    username = input('请输入你的用户名：').strip()
    password = input('请输入你的密码：').strip()
    if username=='tanailing' and password == '123456':
        print('欢迎%s登陆,今天的日期是%s'%(username,datetime.datetime.today()))
        break
    elif username=='' or password =='':
        print('账号和密码都不能为空！')
    else:
        print('账号/密码错误')
else:
    print('错误次数过多')


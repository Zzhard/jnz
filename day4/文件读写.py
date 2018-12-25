
# r  只读，打开文件不存的话，会报
# w  只写，会清空原来文件的内容
# a  追加写，不会请求，打开的文件不存在的话，也会帮你新建一个文件

# r+  读写模式
# w+   写读模式
# a+    追加读模式

#  rb  wb  ab+
# r+和w+分别试一下能不能读写，r+打开不存在的文件是否会报错
# f = open('users2.txt','a+',encoding='utf-8')
# f.seek(0)
# print(f.read())
# f.write('a+模式')
# f.write('hahaha')
# print('读',f.read())#获取到文件里面所有的内容
# print(f.readlines())#获取到文件里面所有的内容
# print(f.readline())#读取一行
# print(f.readline())
# print(f.readline())


# a=['username1,12345\n','username2,123456\n']
# # for i in a:
# #     f.write(i+'\n')
# u='abc,123'
# f.writelines(u)

#file('a.txt','w') #python2

# https://aliuwmp3.changba.com/userdata/video/35026AD35B136F789C33DC5901307461.mp4


#1、有个文件
#2、打开文件
#3、操作文件 读、写
#4、关闭

#只读模式，默认的
#写模式
#追加模式
# w是会清空文件内容
f = open('users.txt','a+')
f.seek(0)#移动文件指针
print(f.read())#获取到文件里面所有的内容
f.write('yangfan,12345\n')
f.write('mayanyan,12345\n')
f.flush()#
f.close()
#文件指针。
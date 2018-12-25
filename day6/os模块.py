import os
# os.rename(old,new)#重命名
# os.remove(f)#删除文件

# os.mkdir('china/beijing') #创建文件夹
# os.makedirs('china/beijing') #父目录不存在的时候会帮你创建
# os.removedirs('china')#只能删除空文件夹

# print(os.listdir())#显示该目录下面的所有文件和文件夹
# print(os.path.isdir('china1'))#判断是否是文件夹
# print(os.path.isfile('china'))#判断是否是文件
# print(os.path.exists('china'))#判断文件或者文件夹是否存在
# res = os.system('ipconfig')#执行操作系统命令 ls]
# print('res...',res)
# res = os.popen('ipconfig').read()#用来执行操作系统命令
# print(res)
# print(os.path.join('china','beijing','haidian','changping','a.py'))#拼路径
res = os.path.split(r'china\beijing\haidian\changping\a.py')#用来分割文件名和路径
# print(res)
res = os.path.dirname(r'china\beijing\haidian\changping\a.py')#取父目录
print(res)
print(os.path.getsize('笔记.txt'))#单位是字节
print(os.getcwd())#取当前的目录
print(os.chdir(r'C:\Users\nhy\PycharmProjects\jnz\day5'))#进入到哪个目录下
print(os.getcwd())#取当前的目录
#分别用他们2个创建一个2层的牡蛎

# china/beijing

# 统计e盘下面有多个python文件

# res = os.walk(r'china')
# count = 0
# for cur_path,dirs,files in res:
#     print(cur_path)
#     #china/a.py
#     for f in files:
#         if f.endswith('.py'):
#             # count+=1
#             os.remove(os.path.join(cur_path,f))
# print(count)
#
#
# def find_file(path,keyword):
#     #查找文件的
#     res = os.walk(path)
#     for cur_path, dirs, files in res:
#         for file_name in files:
#             if keyword in file_name:
#                 print('该文件在 %s下面' %cur_path)
#
#e:\\xxx"\xxx
#/user/loal/xxx
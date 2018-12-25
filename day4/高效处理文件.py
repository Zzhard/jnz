f = open('users.txt',encoding='utf-8')
#文件对象、文件句柄
#第一种方式：
# while True:
#     line = f.readline()
#     if line!='':
#         print('line:',line)
#     else:
#         print('文件内容都读完了，结束了')
#         break


for line in f:
    print(line)

#1、简单、粗暴直接的
# f = open(r'C:\Users\nhy\Desktop\file.txt',encoding='utf-8')
# res = f.read().replace('一点','二点')
# f.close()
# f = open(r'C:\Users\nhy\Desktop\file.txt',mode='w',encoding='utf-8')
# f.write(res)
# f.flush() #立即把缓冲区里面的内容，写到磁盘上
# f.close()

# f = open('file.txt','a+',encoding='utf-8')
# f.seek(0)
# res = f.read().replace('你','NI')
# f.seek(0)
# f.truncate() #清空文件里面的内容
# f.write(res)
# f.close()
#缓冲区  a
import os
# f = open('file.txt',encoding='utf-8')
# f2 = open('file.txt.bak','w',encoding='utf-8')
# for line in f:
#     new_line = line.replace('一点','二点')
#     f2.write(new_line)
# f.close()
# f2.close()
# os.remove('file.txt')
# os.rename('file.txt.bak','file.txt')

with open('file.txt',encoding='utf-8') as f, open('file.txt.bak','w',encoding='utf-8') as f2:
    for line in f:
        new_line = line.replace('二点','一点')
        f2.write(new_line)

os.remove('file.txt')
os.rename('file.txt.bak','file.txt')


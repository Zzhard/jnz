s='abcdef'

users = ['username','user2','user3']
# username,user2,user3

# res = ','.join(users)#1、把list变成了字符串 2、把list里面每一个元素用逗号连接起来
# print(res)
# print(s.find('z'))#返回-1
# print(s.index('z'))#报错
# print(s.count('z'))
# print('0'.isdigit())#判断是否为正整数
# print(s.islower())
# print(s.isupper())
print('acbe123'.isalnum()) #判断字符串里面有英文或者有数字。
#aaaAfd  true
#1223432  true
#acas12323  true
#sdf&*(    false

print('acbe'.isalpha()) #只能是字母
#都是字母才返回ture

# print(s.isspace())#判断是否的空格
# s.splitlines()#以换行符分割字符串
#都是找元素的下标，先分别用他们去找存在的元素，再找不存在的

# l = list(range(1,110))
# new_l = []
# for i in l:
#     si=str(i)
#
#     # if len(si)==1:
#     #     new_i = '00'+si
#     # elif len(si) == 2:
#     #     new_i = '0'+si
#     # else:
#     #     new_i = si
#     new_l.append(si.zfill(5))
# print(new_l)
# 001 ,002,003 012,100 ,101

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)

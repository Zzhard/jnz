password='jpg 12345456789 .jpg ABCDE'
# print(password)
new_password = password.strip('.jpg') #默认去掉字符串两边的空格和换行符
# print(password.lstrip())
# print(password.rstrip())
# print('password',password)
# print('newpassword',new_password)
# print(password.upper())#转成大写的
# print(password.lower())#转成小写的
# print(password.capitalize())#吧首字母改成大写的
# print(password.count('jpg'))
# print(password.replace('谭爱玲','上山打老虎'))#替换字符串
# filename = 'a.mp4'
# age=18
# print(filename.endswith('.mp3'))#判断是否以xx结尾
# print(filename.startswith('186'))#判断是否以开头
# print('{name},{age}'.format(name='hhh',age=age))

names = '小军 海龙 杨帆      谭爱玲'
# print(names.replace(' ',''))
print(names.split(','))
#1、是吧字符串变成list2、以某个字符串分割，分割之后的是list里面的每一个元素
# a = True   #布尔类型 ，真
# b = False  #假，条件不成立
# if filename.endswith('.mp3'):
#     pass
# else:
#     print('')
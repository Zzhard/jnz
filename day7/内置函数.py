# input()
# type()
# len()
# print()
# enumerate()
# list()
# dict()
# tuple()
# set()
# str()
# int()
# float()
# bool()
# print(max([1,2,3,4,7,8,9]))
# print(min(1,2,3,4,7,8,9))
# print(round(3.1323432,2)) #取几位小数
# sorted([5,6,7,343])
s='1223423423'

# print(sorted(s,reverse=True))

# print(ord('a'))#字母转成阿斯克码表里面的值
# print(chr(97))#把数字转成阿斯克码表里面的字母

res = any([1,1,0]) #如果这个list里面有一个为真，就返回true
# print(res)
res = all([1,1,1,1,1]) #如果这个list里面全部为真，就返回true
print(res)

# import hashlib
# print(dir(hashlib))
# m = hashlib.md5('abcd'.encode())
# print(dir(m))
# print(m.hexdigest())
# f = open('a.txt').read()
# print(type(f))
# res = eval(f) #执行简单的python代码
# print(res)
# print(type(res))

my_code= '''
def my():
	print('运行my，xioaojun')
my()
'''
# exec(my_code) #执行python代码的

# map()

# filter()

# l2 = []

# def bl(i):
#     return str(i).zfill(2)
#
# l='12345677'
# res = set(map(bl,l))  #map是循环帮你调用函数，然后保存函数的返回值的，放到一个list里面
# print(res)
l='12345677'

def bl(i):
    # return str(i).zfill(2) #  '01'
    if i>'3':
        return True

# m = list(map(bl,l))
f = list(filter(bl,l)) #filter也是循环调用函数的，如果函数返回的值是真，那么就保存这个值
# print(m)
print(f)




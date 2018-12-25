import copy
# l = [1,1,1,2,3,4,5]
#     #1 1,2,3,4,5
#     #0 1 2 3 4 5 6
# # l2=[1,1,1,2,3,4,5]
# # l2 = copy.deepcopy(l)# 深拷贝
#
# l2 = l #浅拷贝
# #l2 = l.copy() #浅拷贝
#
# print(id(l))
# print(id(l2))
# for i in l2:
#     if i%2!=0:
#         l.remove(i)
# print(l)
#循环删list的时候，会导致下标错位，结果是不对的

a='tanailing'
b = a
a='niuniu'

print(a)
print(b)
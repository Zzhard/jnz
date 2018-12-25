# int float list str dict tuple bool set

#集合,
    # 1、天生可以去重
    # 2、集合是无序
l=[1,1,2,2,3,3]
res = set(l)
l = list(res)
print(res)
{1, 2, 3}

jihe = set() #定义一个空的集合


xingneng =['tanailing','杨帆','liurongxin','小黑']
zdh = ['tanailing','杨帆','liurongxin','小军','海龙']
xingneng = set(xingneng)
zdh = set(zdh)
# res = xingneng.intersection(zdh)#取交集
# res = xingneng &  zdh   #取交集
# res = xingneng.union(zdh) #取并集，把2个集合合并到一起，然后去重
# res = xingneng | zdh
#差集
# res = xingneng.difference(zdh) #取差集，在a里面有，在b里面没有的
# res = xingneng - zdh #取差集
#对称差集
# res=xingneng.symmetric_difference(zdh)#两个里不重复的值
# res = xingneng ^ zdh
print(res)
import string
l1 = set(string.ascii_lowercase)
print(l1)
# l2 = {'a','b','c'}
l2={1,2,3}
# print(l2.issubset(l1))
# print(l1.issuperset(l2))
# print(l1.isdisjoint(l2)) #有交集返回false，没有交集返回true
# print(l2)
# print(list3.issubset(list1))  # 判断list3是不是list1的子集
# print(list1.issuperset(list3))  # 判断list1是不是list3的父集
# print(list1.isdisjoint(list3))  # 判断list1和list3是否有交集

l2.add('s')#添加元素
# l2.remove('a')#删除指定的元素
l2.pop()#随机删除一个元素
for l in l1:
    print(l)
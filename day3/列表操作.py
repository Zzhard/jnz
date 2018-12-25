names='崔海龙 杨帆 刘荣心.....'
# list 列表 数组 array
            # 0      1     2         3
stu_name = ['崔海龙','杨帆','刘荣心',1,1.5]
#下标、索引、角标
#计算机里面起始都是从0开始的
print(stu_name)
#增删改查
stu_name.append('杨月')#在list的末尾添加一个元素
stu_name.insert(0,'小军')#指定位置添加元素
# stu_name.insert(0,'小军')#指定位置添加元素
print('修改之前的',stu_name)

#改
stu_name[5]='孔垂顶'
print('修改之后的',stu_name)

# 删
# stu_name.append('小军')
# print(stu_name)
# stu_name.remove('小军')#
# print(stu_name)
# stu_name.pop()#删除最后一个元素
# stu_name.pop(4)#删除指定下标的元素
# stu_name.remove('小军')#删除指定的元素，
# 如果有一样的元素，只会删除第一个
# stu_name.pop(18)#删除指定下标的元素
# print(stu_name)
# del stu_name[-1]
# print(stu_name)

#查
my_list = ['小黑','小白',1,1,2,1.5]
print(my_list[-1])
print(my_list[0])
print(my_list.count(5)) #查询某个元素在list里面出现的次数
print('index方法：',my_list.index(1))#查找元素的下标，元素不存在的话，会报错
print('reverse:',my_list.reverse())#reverse是反转list
print(my_list)
# my_list.clear()#清空整个list
# print(my_list)
nums =[9.23,9,3,6,1,0]
nums.sort(reverse=True)#排序,如果指定了reverse=True，那么就是降序
# nums.extend(my_list)#把一个list里面的元素加入进去
print(nums)
new_list = nums + my_list + stu_name
print(new_list)
print(new_list * 3) #复制几个



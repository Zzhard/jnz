# stu_name=['stu1','stu2','stu3','1','1.5']
#
# #列表的增删改查
#
# #增,append方法是在末尾添加，insert(下标,'')方法在指定位置向列表添加数据
# stu_name.append('stu4')
#
# stu_name.insert(0,'hahha')
# print(stu_name)
# #改,对指定下标进行修改
# stu_name[1]='xiaohei'
#
# print(stu_name)
# #查,使用下标方法
# print(stu_name[5])
# #删除
# # stu_name.pop(10) #使用pop方法通过下标删除，但是可能会出现下标越界，报错
# # stu_name.remove('stu2') #使用remove方法直接删除指定元素,如果元素不存在不会报错
# del  stu_name[0] #del方法和pop()差不多一样
# print(stu_name)

"""list列表的其他操作"""
#count()计算列表中有多少个相同元素

stu_name=['stu1','11','aabb','ccdd','aabb']

print(stu_name.count('aabb'))

print(stu_name.index('aabb')) #使用index()方法通过元素查找到元素下标





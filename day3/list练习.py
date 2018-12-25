
users = ['nhy','haha']

#校验手机号是否存在的
# for i in range(5):
#     username = input('请输入用户名：')
#     #如果用户不存在的话，就说明可以注册，
#     # if users.count(username)>0:
#     if username not in users:  #in就是判断在不在里面
#         print('用户未注册,可以注册')
#         users.append(username)
#     else:
#         print('用户已注册')

nums1=[1,2,3] #一维数组
nums2=[1,2,3,[4,56]] #二维数组
# print(nums2[-1][-1])
nums=[1,2,3,4,['a','b','c','d','e',['一','二','三']],['四','五']] #三维数组
# nums=[1,2,3,4,['a','b','c','d','e',['一','二','三',[1,2,3]]]] #四维数组

#多维数组，
#菊花 二
#李猛 五
# print(nums[4][5][1])
# print(nums[5][1])
# users = ['nhy','haha']

passwords=['123456','123123','7891234','password']
# print(len(passwords)) #取长度，也就是list里面元素的个数
#循环这个list
# count = 0#最原始list取值方式，是通过每次计算下标来获取元素的
# while count<len(passwords):
#     s = passwords[count]
#     print('每次循环的时候',s)
#     count+=1

# passwords=['123456','123123','7891234','password']
# index = 0
# for p in passwords:#for循环直接循环一个list，那么循环的时候就是每次取它的值
#     passwords[index] = 'abc_'+p
#     index+=1
# print(passwords)

# passwords=['123456','123123','7891234','password']
# for index,p in enumerate(passwords):#使用枚举函数，它会帮你计算下标和元素
#     passwords[index] = 'abc_' + p
# print(passwords)


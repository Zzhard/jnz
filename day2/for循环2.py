# for hhh in range(9):
#     print(hhh)

#字符串格式化
import datetime
name = '谭爱玲'
today = datetime.date.today()
welcome1 = '%s，周末了，亲手为家人泡上一道茶吧。' \
           '今天的日期是%s'%(name,today)
print(welcome1)

# name2 = '捶捶'
# print(name+'爱'+name2)

# words = '你的名字是 %s  你的年龄是 %s 你的分数是 %s'%(name,28,17.3)
# words2 = '你的名字是 %s  你的年龄是 %d 你的分数是 %.2f'%(name,89,19.88)
# print(words2)

# sql='insert into student (id,name,age,addr,phone,sex,qq,email) values ' \
#     '("%s","%s","%s","%s","%s","%s","%s","%s");'
#
# sql2 = 'insert into student (id,name,age,addr,phone,sex,qq,email) values' \
#        ' ({id},{name},{age},{addr},{phone},{sex},{qq},{email})'
#
# sql3 = sql2.format(id=1,name='谭爱玲',age=18,sex='111',phone=111111,qq=222,email=33,addr='北京')
# print(sql3)
words = '你的名字 {name} 你的年龄 {age}'.format(name='小黑',age=18)
print(words)
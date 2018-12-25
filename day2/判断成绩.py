# 输入一个分数 大于等于90 优秀
#小于 90 大于等于80 良好
#大于等于60 小于80 及格
#小于60，不及格
score = input('请输入你的成绩：')
# raw_input()
#用input接收到的类型全部都是字符串
print('score的类型',type(score))
score = int(score)#类型转换
print('score的类型',type(score))
if score >= 90 :
    print('优秀')
elif score<90 and score>=80:
    print('良好')
elif score>=60 and score<80:
    print('及格')
else:
    print('不及格')
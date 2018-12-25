import random
num = random.randint(1,100) #随机产生的数字
print(num)
#代码都是从上到下运行
count = 0
while count<7:
    count+=1
    guess = input('请输入一个数字：')
    guess = int(guess) #转成int类型
    if guess>num:
        print('猜大了')
    elif guess==num:
        print('恭喜你，猜对了')
        break
    else:
        print('猜小了')
else:
    print('错误次数过多')

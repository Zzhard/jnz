#模块
# 1、标准模块,不需要你单独安装，python自带的模块
# 2、第三方模块
# 3、自己写的python
#一个python文件就是一个模块
import random
print(random.randint(100000,999999)) #随机取一个整数
print(random.uniform(1,900))#取一个小数
stus = ['xiaojun','hailong','yangfan','tanailing','yangyue','cc']
print(random.choice('abcdefg'))#随机取一个元素
print(random.sample(stus,2)) #随机取N个元素

l = list(range(1,101))
print('洗牌之前的',l)
print(random.shuffle(l))#洗牌,这个就只能传list了
print('洗牌之后的',l)

import datetime

def get_today():
    print(datetime.datetime.today())
name = 'wangcan'#全局变量
names = []
def get_name():
    # global name
    names.append('hahaha')
    name = 'hailong'
    print('1、函数里面的name',name) #2 wangcan hailong hailong
def get_name2():
    global name

    print('2、get_name2',name)#1 hailong wangcan wangcan
get_name2()
get_name()
print(names)

print('3、函数外面的name',name) # 3、hailong wangcan hailong



money = 500
def test(consume):
    return money - consume

def test1(money):
    return test(money) + money

# money = test1(money)
# print(money)


def test():
    global a
    a = 5

def test1():
    c = a + 5
    return c
# test()
res = test1()
print(res)
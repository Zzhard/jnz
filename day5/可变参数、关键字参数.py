def my(name,sex='女'):
    #name 必填参数、位置参数
    #sex 默认值参数
    #可变参数
    #关键字参数
    pass

def send_sms(*args):
    #可变参数，参数组
    #1、不是必传的
    #2、它把传入的元素全部都放到了一个元组里面
    #3、不限制参数个数
    #4、它用在参数比较多的情况下
    for p in args:
        print(p)

#关键字参数

def send_sms2(**kwargs):
    #1、不是必传的
    #2、不限制参数个数
    print(kwargs)

send_sms2()
send_sms2(name='xiaohei',sex='nan')
send_sms2(addr='北京',country='中国',c='abc',f='kkk')

#1、不传参数
#2、传1个
#3、传N个

#1、是不是必传的
#2、传入多个参数的时候，它把参数保存到了哪里
# send_sms()
# send_sms(1861231231)
# send_sms(1861231231,121342,1231231,1232342,42342342)

def my(name,country='China',*args,**kwargs):
    #1、位置参数 2、默认值参数 3、可变参数 4、关键字
    print(name)
    print(country)
    print(args)
    print(kwargs)
# my('xiaojun','Japan','beijing','天通苑',color='红色',
#    age=32)

# my('xiaojun','beijing','天通苑',
#    color='红色',age=32)


#递归的意思函数自己调用自己
#递归最多递归999
count = 0
# def say():
#     global count
#     count+=1
#     print('say')
#     print(count)
#     say()
# say()#
# def test1():
#     num = int(input('please enter a number：'))
#     if num%2==0:#判断输入的数字是不是偶数
#        return True #如果是偶数的话，程序就退出了，返回true
#     print('不是偶数请重新输入！')
#     return test1()#如果不是偶数的话继续调用自己，输入值
# print(test1())#调用test

def db_connect(ip,user,password,db,port):
    print(ip)
    print(user)
    print(password)
    print(db)
    print(port)

db_connect(user='abc',port=3306,db=1,
           ip='sdfsd',password='sdfsd')
db_connect('192','root',
           db=2,password='123456',port=123)

# db_connect(password='123456',user='192.468',
#            'sdfsdf','sdfsdf','sdfsd')#不对的

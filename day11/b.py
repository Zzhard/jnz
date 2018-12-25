class People: #新式类
    eye = 2
    mouth = 1
    shengao = 180
    money=1000000
    def __init__(self,name):
        self.name = name
        #构造函数，类在初始化做的一些操作
        print('造了一个人，这个人是%s'%name)
    def cry(self):
        print('哭。。。')
    def makeMoney(self):
        print('self的内存地址',id(self))
        print('%s 挣了20w'%self.name )

xiaojun = People('小军') #实例化
# print('小军的内存地址',id(xiaojun))
xiaojun.makeMoney()
# People.makeMoney(xiaojun)

# hailong = People('海龙')
# print('海龙的内存地址',id(hailong))
# hailong.makeMoney()




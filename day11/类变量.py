class People:
    country = 'China' #类变量
    def __init__(self,name,sex):
        self.name = name  #实例变量
        self.sex = sex
    def say(self):
        print('name '+self.name)
        print('sex'+self.sex)
        print('country'+self.country)

    @property  #把一个函数变成一个变量，这个变量的值就是函数的返回值
    def get_name(self):
        return self.name

print(People.country)
xiaojun = People("xiaojun",'男')
xiaojun.say()
print(xiaojun.get_name)
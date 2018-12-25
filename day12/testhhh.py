# class Person:
#     def __init__(self,name,sex):
#         #构造函数
#         self.name = name
#         self.sex = sex
#     def say(self):
#         print('%s 说话'%self.name)
#         print('%s 说话'%self.sex)
#     def cry(self):
#         print('cry')
#     def run(self):
#         print('run')
#     def sleep(self,t):
#         import time
#         time.sleep(t)
#
#

# def person(name,weight,action):
#     if action=='run':
#         weight = weight - 1
#     elif action=='eat':
#         weight = weight + 2
#     print('%s 的体重是 %s'%(name,weight))
#     return weight
# new_weight = person('小明',500,'吃饭')
# new_weight = person('小明',new_weight,'跑步')
# new_weight = person('小明',new_weight,'跑步')
# new_weight = person('小明',new_weight,'跑步')

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.tizhong =  weight
    def eat(self):
        self.tizhong +=2
        self.print
    def run(self):
        self.tizhong -= 1
        self.print
    @property
    def print(self):
        print("【%s】的体重是 【%s】"%(self.name,self.tizhong))

# xj = Person('小军',120)
# xj.run()
# hl = Person('hailong',150)
# hl.run()
# hl.run()

#
class MyStr:
    def __init__(self,s:str):
        self.s = str(s)
    def replace(self,old,new):
        return self.s.replace(old,new)
    def strip(self):
        return self.s.strip()
    def split(self,seq=''):
        return self.s.split(seq)

s = MyStr(123456)
news = s.replace('1','2')
print(news)
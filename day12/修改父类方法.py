class Lw:
    def about_me(self,name):
        print('[%s] 会抽烟喝酒烫头'%name)
        print('[%s] 会抽烟喝酒烫头'%name)
        print('[%s] 会抽烟喝酒烫头'%name)
        print('[%s] 会抽烟喝酒烫头'%name)

class Xw(Lw):
    def about_me(self,name,age):
        super().about_me(name) #spuer指的就父类
        print('age',age)

    def abc(self):
        pass



wxm = Xw()
wxm.about_me('王小明',18)

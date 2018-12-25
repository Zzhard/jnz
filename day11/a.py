class Car:
    def __init__(self,color,pl):
        self.color = color
        self.pl = pl
    def add_fun(self,fun):
        self.fun = fun
        print('颜色是%s'%self.color)
        print('排量是%s'%self.pl)

    def help(self):
        print('这个汽车的颜色【%s】'%self.color)
        print('这个汽车的排量【%s】'%self.pl)
        print('这个汽车的功能【%s】'%self.fun)

BMW=Car('红色','3.5L')
# BMW.add_fun('水陆两栖')
BMW.help()
# add_fun(BMW,)


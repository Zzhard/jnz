class Phone:
    def __del__(self):
        print('哈哈哈哈')
    def call(self,name):
        print('为%s打call，为%s打电话！'%(name,name))
    def __init__(self):
        self.test = 'abc'
        print('我是构造函数')

iphonx = Phone()
print(iphonx.test)
iphonx.call('小军')
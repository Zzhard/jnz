class Demo(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print(self.name)
Demo('dsx')()
class Lw:
    money = 100000
    house = '10套'
    def driver(self):
        print('开车')
    def chouyan(self):
        print('抽烟')
    def hejiu(self):
        print('喝酒')
    def tangtou(self):
        print('烫头')

class Xw(Lw):
    def huaqian(self):
        print('花钱。。。')

class Student():
    def sql(self):
        print('sql')
    def linux(self):
        print('linux')

class PyStudent(Student):
    def python(self):
        print('python')

class XnStudent(Student):
    def xn(self):
        print('xn')
    def sql(self):
        print('sql....')
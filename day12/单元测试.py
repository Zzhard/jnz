
# res = calc(2,2)

#unittest
#junit
#phpunit
import unittest

def calc(a,b):
    return  a+b

class MyTest(unittest.TestCase):
    def testa(self):
        res = calc(1,2)
        self.assertEqual(3,res,msg='预期结果和实际结果不一致')
    def testb(self):
        res = calc(0,1)
        self.assertEqual(2,res,msg='预期结果和实际结果不一致')

# unittest.main()
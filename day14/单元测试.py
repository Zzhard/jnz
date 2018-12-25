import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport
class MyTest(unittest.TestCase):
    def setUp(self):
        #每条用例执行之前会执行setup
        print('这是setup')
    def tearDown(self):
        #每条用例执行之后都会执行teardown
        print('这是teardown')

    @classmethod
    def setUpClass(cls):
        #这个类里面的用例执行之前，最先执行它，最前面
        print('这是setupclass')

    @classmethod
    def tearDownClass(cls):
        #这个类里面所有的用例执行完之后执行它，最后面
        print('tearDownClass')


    def test_reg(self):
        '''注册'''
        print('reg')
        self.assertEqual(1,2,msg='token不对')
    def test_login(self):
        '''登录'''
        print('login')
        self.assertEqual(1,1)
    def test_buy(self):
        self.assertEqual(1,2,msg='购买失败')
    def test_z(self):
        self.assertIn(1,[1,23])
    def test_assert(self):
        res = False
        self.assertFalse(res,)
        print('test_assert')


#下面这一坨是产生不好看的报告
# f = open('report.html','wb')
# runner = HTMLTestRunner.HTMLTestRunner(f,title='nhytest',
#                                        description='xxx接口测试')
# sutie = unittest.makeSuite(MyTest)#变成测试集合
# runner.run(sutie)


suite = unittest.makeSuite(MyTest)#变成测试集合
report = BeautifulReport(suite)
report.report(filename='bfreport.html',description='接口测试报告')

# 测试用例
# 测试集合 testsuite  多个用例放在一起
# testrunner  运行用例的
# testloader  查找测试用例



import unittest
from parameterized import parameterized
def login(username,password):
    print(username,password)
    print('=============')
    return 1

class MyTest(unittest.TestCase):
    @parameterized.expand(
        [
           ['xiaodong','123','success'],
           ['yangfan','456','fail'],
           ['hailong','1273','success'],
           ['liurongxin','1273','success'],
        ]
    )
    def test_login(self,username,passwd,check):
        '正常登陆'
        res = login(username,passwd)
        self.assertEqual(check,res)

unittest.main()
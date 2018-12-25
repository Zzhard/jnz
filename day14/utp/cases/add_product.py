
import unittest
from parameterized import parameterized
from core.my_requests import MyRequest
from core.tools import get_real_value

class MyTest(unittest.TestCase):

    @parameterized.expand('login.xls')
    #[[url,post,param,check]]
    def testpost(self,url,method,param,key,check,):
        r = MyRequest(url,param)
        if method=='post':
            result = r.post()
        else:
            result = r.get()
        res= get_real_value(result,key)
        self.assertEqual(check,res)





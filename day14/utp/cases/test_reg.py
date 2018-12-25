import unittest
from parameterized import parameterized
from core.my_requests import MyRequest
from core.parse_param_file import textFileToList
from conf.setting import default_host
from core.tools import get_real_value
class MyTest(unittest.TestCase):
    @parameterized.expand(textFileToList('reg_data.txt'))
    def test_login(self,username,passwd,key,check):
        '正常登陆'
        url = default_host+'/api/user/login'
        data = {'username':username,'passwd':passwd}
        r = MyRequest(url,data)
        response = r.post()
        res = get_real_value(response,key)

        self.assertEqual(check,res)


import unittest
from conf.setting import default_host
from core.my_requests import MyRequest
from core.tools import mysql,get_real_value
from core.tools import r as redis
class Cj(unittest.TestCase):

    password = 'aA123456'
    username = 'autotest_nhy77910'
    def reg(self):
        '''注册接口'''
        url = '/api/user/user_reg'
        new_url = default_host + url
        data = {'username':self.username,'pwd':self.password,
                'cpwd':self.password}
        r = MyRequest(new_url,data)
        result = r.post()
        self.assertEqual(1,result.get('status'),msg='注册接口不通，%s'%result.get('data'))
        #校验接口是不是通的
        error_code = result.get('data').get('error_code')
        self.assertEqual(0,error_code,msg='注册失败，%s'%result.get('data'))
        sql ='select * from app_myuser where username = "%s";'%self.username
        sql_res = mysql.execute_one(sql)#执行sql
        self.assertIsNotNone(sql_res) #判断数据库返回的是否为空

    def login(self):
        '''登录接口'''
        url  = default_host + '/api/user/login'
        data = {'username':self.username,'passwd':self.password}
        r = MyRequest(url,data)#发请求
        result = r.post()
        self.assertEqual(1,result.get('status'),msg='登录接口不通，%s'%result.get('data'))
        sign = get_real_value('sign',result)#从返回值里面取到sign的值
        self.assertIsNotNone(sign,msg='登录失败:%s'%result)#校验sign
        userid  = get_real_value('userId',result)#从返回值里面取到userid的值
        return userid,sign
    def choujiang(self):
        '''抽奖接口'''
        url = default_host+'/api/product/choice'
        userid,sign = self.login()
        data = {'userid':userid,'sign':sign}
        r = MyRequest(url,data)
        result = r.get()
        self.assertEqual(1, result.get('status'), msg='抽奖接口不通，%s' % result.get('data'))
        redis_key ='choujiang:%s'%self.username
        count = redis.get(redis_key) #操作redis，取key
        self.assertEqual('1',count,'抽奖次数错误%s'%result)
        sql='select count(*) as cishu  from app_record where user_id = %s ;'%userid
        cishu = mysql.execute_one(sql).get('cishu') #执行sql
        # {'cishu':1}
        self.assertEqual(1,cishu,'抽奖记录没有落到数据库里面！')
    def test_choujiang(self):
        '''抽奖流程测试'''
        self.reg()
        self.choujiang()

    @classmethod
    def tearDownClass(cls):
        ##数据清除的工作
        sql='delete from app_myuser where username="%s" ;'%cls.username
        mysql.execute_one(sql)
        key='choujiang:%s'%cls.username
        redis.delete(key)
        print('测试数据清理完成。。')



















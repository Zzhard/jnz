import random
import string
import time
class ParseParam:
    #这个类是用来解析请求参数的
    func_map = ['phone','email','id_card','cur_time','money']
    #映射函数的
    def __init__(self,param):
        self.param = param
        self.parse()
    def phone(self):
        phone_starts = ['134','181','138','177','150','132','188','186','189','130','170','153','155']
        start = random.choice(phone_starts)
        end = str(random.randint(0,99999999))
        res = start+ end.zfill(8)
        return res
    def email(self):
        email_end=['163.com','qq.com','126.com','sina.com']
        end = random.choice(email_end)
        start_str='ATP_test_'
        email_start = ''.join(random.sample(string.ascii_letters+string.digits,6))
        return start_str+email_start+'@'+end
    def id_card(self):
        '''这个产生身份证号的'''
        return 410881199011212121
    def cur_time(self):
        return int(time.time())
    def order_id(self):
        '''从数据库里面获取'''
        pass
    def session_id(self):
        '''从redis里面获取的'''
        pass
    def money(self):
        return 10000
    def parse(self):
        for func in self.func_map:
            temp = str(getattr(self,func)()) #手机号
            self.param = self.param.replace('<%s>'%func,temp)
    def strToDict(self):
        #这个函数是把请求参数转成字典的
        data ={}
        pl = self.param.split(',')
        for p in pl:
            temp = p.split('=')
            if len(temp)>1:
                key,value = temp
                data[key] = value
        return data



if __name__ == '__main__':
    param = 'username=niuhanyang' \
            ',phone=<phone>,email=<email>' \
            ',id_card=<id_card>,start_time=' \
            '<cur_time>,balan=<money>'
    p = ParseParam(param)
    data = p.strToDict()
    print(data)
    # print(p.phone())
    # res = getattr(p,'money') #获取一个对象里面的属性（方法、变量）


    # # print(res())
    # import os,requests
    # res = hasattr(requests,'get')#判断某个模块、类下面有没有某个方法或者变量
    # print(res)
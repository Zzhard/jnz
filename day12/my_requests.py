import requests
import nnlog
class MyRequest:
    log_file_name  = 'MyRequest.log'#日子文件名
    time_out = 10 #请求超时时间
    def __init__(self,url,data=None,headers=None,file=None):
        self.url = url
        self.data = data
        self.headers = headers
        self.file = file
    def post(self):
        try:
            req = requests.post(self.url,data=self.data,headers=self.headers,
                                files=self.file,timeout=self.time_out)
        except Exception as e:
            res = {"status":0,"err_msg":e.args}  #0代表请求失败
        else:
            try:
               res = {"status":1,"data":req.json()} #1代表返回的json
            except Exception as e:
                res = {"staus":2,"data":req.text} #2代表返回不是json
        log_str = 'url： %s 请求方式：post  data：%s ,返回数据：%s'%(self.url,self.data,res)
        self.write_log(log_str)
        return res

    def get(self):
        try:
            req = requests.get(self.url,params=self.data,headers=self.headers,timeout=self.time_out)
        except Exception as e:
            res = {"status":0,"err_msg":e.args}  #0代表请求失败
        else:
            try:
               res = {"status":1,"data":req.json()} #1代表返回的json

            except Exception as e:
                res = {"staus":2,"data":req.text} #2代表返回不是json
        log_str = 'url： %s get请求 data：%s ,返回数据：%s'%(self.url,self.data,res)
        self.write_log(log_str)
        return res

    @classmethod
    def write_log(cls,content):
        log = nnlog.Logger(cls.log_file_name)
        log.debug(content)



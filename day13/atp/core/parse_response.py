import jsonpath
class ResponseParse:
    seqs = ['!=', '>=', '<=', '=', '<', '>', 'in', 'notin']
    #定义支持的运算符
    def __init__(self,response,check):
        self.response = response
        self.check = check

    def format_check(self):
        #格式化检查信息，分别列出key 运算符 实际结果
        #会返回 [['error_code','=','0'],['name','!=','xxx']]
        format_list = []
        check_list = self.check.split(',')
        for s in check_list:
            for seq in self.seqs:
                if seq in s:
                    if len(s.split(seq))>1:
                        key, value = s.split(seq)
                        temp = [key, seq, value]
                        format_list.append(temp)
                        break
        return format_list

    def get_real_value(self,key):
        #从字典里面获取key对应的value
        res = jsonpath.jsonpath(self.response,'$..%s'%key)
        #$..%s这个是jsonpath这个模块的用法
        if res:
            return res[0]
        return '找不到该key【%s】'%key

    def operation_check(self,real,seq,hope):
        #根据运算符判断结果
        msg = "判断信息：%s %s %s "%(real,seq,hope)
        real = str(real)#为了保持类型一致
        if seq=='=':
            status = real == hope
        elif seq=='!=':
            status = real != hope
        elif seq =='in':
            status = real in hope
        elif seq =='notin':
            status = real not in hope
        else:
            status,msg = self.num_check(real,seq,hope)
        return status,msg

    def num_check(self,real,seq,hope):
        #判断数值类型的
        msg = "判断信息：%s %s %s "%(real,seq,hope)
        try:
            real=float(real)
            hope=float(hope)
        except Exception as e:
            msg = "比较时出错，大小比较只能是数字类型！" \
                  "%s %s %s"%(real,seq,hope)
            status = False
        else:
            if seq=='>':
                status = real > hope
            elif seq =='<':
                status = real < hope
            elif seq == '<=':
                status  = real <= hope
            else:
                status = real >= hope
        return status,msg

    def check_res(self):
        #校验所有的检查点
        check_list = self.format_check()
        all_msg=''
        for check in check_list:#循环所有的检查点
            key,seq,hope = check
            real = self.get_real_value(key)
            status,msg = self.operation_check(real,seq,hope)
            all_msg = all_msg+msg+'\n' #累加提示信息
            if status:
                pass
            else:
                return '失败',all_msg
        return '通过',all_msg



import unittest
from BeautifulReport import BeautifulReport as bf
from conf.setting import CASE_PATH
from core.tools import make_today_dir,send_mail
from core.op_data import bak_db,recover_db
import os
import datetime

content = '''
各位好！
        本次测试结果：总共运行%s条用例，通过%s条，失败%s条。详细信息见附件。
    '''

def run_case():
    # sql_file = bak_db() #备份数据库函数
    suite = unittest.TestSuite() #建测试集合
    cases = unittest.defaultTestLoader.discover(CASE_PATH,'test*.py')
    #去某个目录下找测试用例
    for case in cases:
        suite.addTest(case)  #循环把每个文件里面的case加入到测试集合里面
    report = bf(suite) #运行测试用例

    path = make_today_dir() #创建今天的文件夹，存放报告
    file_name = 'report_%s.html'%datetime.datetime.now().strftime('%H%M%S')#生成新的文件名
    report.report(filename=file_name,description='接口测试',log_path=path)#生成报告

    new_content = content%(report.success_count+report.failure_count,report.success_count,report.failure_count)
    abs_path = os.path.join(path,file_name)
    send_mail(new_content,abs_path)
    # recover_db(sql_file)#恢复数据库


#产生报告
run_case()
import os,sys
res = os.path.abspath(__file__) #取当前文件的绝对路径
base_path = os.path.dirname(os.path.dirname(res))
#取父目录
sys.path.insert(0,base_path)#加入环境变量

from lib.service import server
from lib import user,pay,order
from conf.setting import server_info
server.run(**server_info) #启动服务


import flask
import sys
import time
server = flask.Flask(__name__)

@server.route('/')
def index():
    return '<h1>success</h1>'
if len(sys.argv)>1:
    port = sys.argv[1]
    if port.isdigit():
        server.run(port=port)
    elif port=='--help':
        print('这个python文件的作用是让你发财！')
    elif port=='--time':
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print('端口号必须是整数！')
else:
    print('运行错误！请在运行的时候指定端口号\n'
          '请按照下面的方式运行python文件！\n'
          'python mock_server.py 8989')




#sys.argv的作用是获取到运行python文件时，传入的参数
# python xxx.py --help
# 默认如果运行python文件的时候，不传参数，argv里面只有一个元素
#就是当前这个python文件的文件名
# python  xxx.py

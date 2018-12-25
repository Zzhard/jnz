from lib.service import  server
from lib.tools import my_db
import flask
import json
@server.route('/pay')
def pay():
    return '支付'

@server.route('/table')
def get_table_data():
    #获取某个表里面的数据
    table_name = flask.request.values.get('table_name')
    sql='select * from %s;'%table_name
    res = my_db(sql)
    return json.dumps(res,ensure_ascii=False)




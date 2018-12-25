from lib.service import server


server.route('/order',methods=['post'])
def create_order():
    return '生成订单'
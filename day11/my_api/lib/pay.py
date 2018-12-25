from lib.service import  server

@server.route('/pay')
def pay():
    return '支付'
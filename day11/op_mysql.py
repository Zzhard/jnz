import pymysql

class MySQL:
    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        self.conn = pymysql.connect(host=host,user=user,password=password,db=db,port=port,charset=charset)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        #初始化的时候就连接数据库
    def execute_many(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()  # [ {},{}  ]
    def execute_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('连接已经关闭')

db=MySQL('118.24.3.40','jxz','123456','jxz')

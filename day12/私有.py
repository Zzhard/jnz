class DB:
    port = 3306  #类变量
    def __init__(self):
        self.host = '127.0.0.1'
        self.__user = 'root'  #实例变量，成员变量
        self.__password = '123456'
        self.db = 'xx'
        # self.__help()
    def sql(self,sql):
        self.__help()
        print('执行sql')
    def __help(self):
        print(self.host)
        print(self.__user)
        print(self.__password)
        print(self.db)
        print(self.port)

    def get_port(self):  #实例方法
        print(self.port)

    @classmethod
    def help(cls):
        print('这个类是用来连接数据库的，它的用法是xxx')
        print('cls的内存地址',id(cls))

DB.help()


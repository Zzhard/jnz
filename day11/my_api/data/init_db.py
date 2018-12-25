from lib.tools import my_db

sql = open('init.sql').read()
my_db(sql)
print('sql执行完成')
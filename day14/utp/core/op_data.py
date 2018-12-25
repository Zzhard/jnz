import os
from conf.setting import mysql_info,SQL_PATH
from core.tools import mysql
import datetime
def get_mysql_info():
    user = mysql_info.get('user')
    password = mysql_info.get('password')
    host = mysql_info.get('host')
    db = mysql_info.get('db')
    port = mysql_info.get('port')
    return user,password,host,db,port

def bak_db():
    user, password, host, db, port = get_mysql_info()
    sql_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.sql'
    sql_filename = os.path.join(SQL_PATH,sql_filename)
    command = 'mysqldump -u{user} -p{pwd} -P{port} -h{host} {db} > {file}'.format(
        user=user,pwd=password,port=port,host=host,db=db,file=sql_filename
    )#执行备份数据库命令
    os.system(command)
    print('数据备份完成！')
    return sql_filename

def recover_db(sql_filename):
    user, password, host, db, port = get_mysql_info()
    new_db = db+'_'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    sql='RENAME database %s TO %s; '%(db,new_db)#给原来的数据库改名
    mysql.execute_one(sql)
    print('数据库改名')
    sql2='create database %s charset utf8;'%db
    mysql.execute_one(sql2)
    print('新的数据库已经创建%s'%db)
    command = 'mysql -u{user} -p{pwd} -P{port} -h{host} {db} < {file}'.format(
        user=user, pwd=password, port=port, host=host, db=db, file=sql_filename
    )
    os.system(command)
    print('数据库恢复完成！')









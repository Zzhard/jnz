import pymysql

def my_db(sql):
    conn = pymysql.connect(
        host='118.24.3.40',
        user='jxz',
        password='123456',
        db='jxz',
        charset='utf8',
        autocommit=True
    )
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res


def check_float(s):
    '''
    这个函数的作用就是判断传入的字符串是否是合法的小数
    :param s: 传入一个字符串
    :return: True/false
    '''
    s = str(s)
    if s.count('.')==1:
        s_split = s.split('.')
        left,right = s_split
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left[1:].isdigit() \
            and right.isdigit():
            return True
    return False
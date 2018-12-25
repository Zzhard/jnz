# 8a10818ac51be3681d5f915041c90092

import hashlib

# import md5 #这个是python2里面的
password='123123'
# print(password.encode())#转成二进制类型的才可以加密
m = hashlib.md5(password.encode())
# m = hashlib.sha1(password.encode())
# m = hashlib.sha224(password.encode())
# m = hashlib.sha256(password.encode())
# print(dir(m))
print(m.hexdigest())
#md5加密之后是不可逆

#撞库
# 123456  4297f44b13955235245b2497399d7a93
# 345678  4297f44b13955235245b2497399d7a93
# 123123  4297f44b13955235245b2497399d7a93

# 123123

#123456+34few45834@$

def my_md5(s:str,salt=None):
    #salt是盐值
    s = str(s)
    if salt:
        s = s+salt
    m = hashlib.md5(s.encode())
    return m.hexdigest()


#加盐

#34few45834@$
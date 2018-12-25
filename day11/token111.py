# import itsdangerous
#
# salt='sdf234^#$@G'
# t = itsdangerous.TimedJSONWebSignatureSerializer(salt,expires_in=30)
# # res = t.dumps({'username':'yangfan','user_id':1})
# # token = res.decode()
# # print(token)
# s='eyJhbGciOiJIUzI1NiIsImlhdCI6MTU0MTgyMDA1NiwiZXhwIjoxNTQxODIwMDg2fQ.eyJ1c2VybmFtZSI6InlhbmdmYW4iLCJ1c2VyX2lkIjoxfQ.FUfs92HuVKrt61AKpMjv1Iye8QDP7XUGOfgcrSusMv8'
# res = t.loads(s)
# print(res)

import pymysql
coon = pymysql.connect()
cur= coon.cursor()
# sqls = ['sleect','uodate','delet','insert']
# for i in sqls:
#     cur.execute(i)
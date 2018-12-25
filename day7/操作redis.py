import redis

ip = '118.24.3.40'
password='HK139bc&*'

r = redis.Redis(host=ip,password=password,port=6379,db=1,
                decode_responses=True)
                # decode_responses这个参数的意思是，返回的二进制数据直接decode一下
print(r.get('python:lyos'))
print(r.hgetall('jnz_stus'))

# r.flushdb() #删除这个数据库里面所有的key
# print(res.decode())   #decode是bytes类型，转成字符串

#string
# res = r.get('nhy2')
# r.set('nhy','acb123',24*60*60) #新增和修改都是它
# r.delete('nhy') #删除指定的key
# r.set('python:os','listdir,path')
# res = r.get('python:os')
# print(res)

# print(r.keys('session*')) #获取所有的key


#哈希类型 hash类型

#二层字典

# r.hset('jnz_stus','yangfan','sdfsdfsdfsdf')
# res = r.hget('jnz_stus','cm') #指定获取里面小key的值
# r.delete('jnz_stus')  #删除大key
# r.hdel('jnz_stus','cm') #删除指定的小key
# res = r.hgetall('jnz_stus') #获取到大key里面所有的数据
# print(res)
# new = {}
# for k,v in res.items():
#     new [k.decode()] = v.decode()
# print('======下面是转完之后的')
# print(new)
# 1、先循环res
# 2、k和v decode一下 然后放到new这个字典里面
# session = {
#     "nhy":{'sex':18,'age':18},
#     "nhy2":{'sex':18,'age':18},
# }
#
# token = {
#     "nhy2":{'x':'x'}
# }

# 0 1

0 - 127
124-125
# 阿斯克码表
# gb2312   #
# gbk #
# JP123 #
# 1123 - 牛
# 1233 - 哈

# unicode 字符集 万国码
#python2
#python3 unicode
    # utf-8
#  a  1
# 牛  2

# s='水电费水电费' #JP231
# s2= s.encode('JP231') #先按照之前的字符集解码
# s2.decode('utf-8') #然后再编码，编成你要的字符集

#两种不同类型的字符集要互相转的话，先转成unicode

# 小军  男 185  29 xxxx 1111 sss@qq.com 2387121
# 海龙  男 185  29 xxxx 1111 sss@qq.com 2387121
# 杨帆  男 185  29 xxxx 1111 sss@qq.com 2387121
# 杨月  男 185  29 xxxx 1111 sss@qq.com 2387121

all_sty = [ ['xioajun','xxx','x'],['xx']  ]
xiaojun = ['xioajun','xxx','x']
hailong = ['xxx']

#。。。。。
# k-v 形式
#字典也可以循环
'''
xiaojun = {
    'name':'xiaojun',
    'sex':'男',
    'shengao':'185',
    'age':18,
    'email':'acb@qq.com',
    'addr':'火星',
    'id':1
}
#优点，速度快，好取值

hailong = {
    'name':'hailong',
    'sex':'男',
    'shengao':'185',
    'age':18,
    'email':'acb@qq.com',
    'addr':'火星',
    'id':2
}


for i in hailong:
    # print(i)
    # if i =='name':
    print(hailong[i])


# for  k,v in hailong.items():
#     print(k,v)




#增删改查

# print(hailong['name'])
# print(hailong.get('zhuzhi','火星')) # get查找-不报错，可以设置默认值

#add
# hailong['zhuzhi'] = '北京'
# hailong['age']=30
# print(hailong)

#delete
# hailong.pop('age')
# print('删除age',hailong)
# hailong.popitem() #随机删除
# print(hailong)

# del hailong['age'] #del 删除
# print(hailong)

# print(hailong.values())

# name = {'zhuzhi':"北京"}
# hailong.update(name)  #字典合并
# print(hailong)
#
# print(hailong.keys())






# 1、设置默认值有啥用
# 2、
stus = {}
#增加
#
stus['name'] = '小军'
stus['name'] = '海龙'
stus.setdefault('name','杨帆')#如果这个key已经存在，那么就不修改它的值了
stus.setdefault('age',18)
stus.setdefault('sex','nan')
stus.setdefault('addr','北京')
stus.setdefault('phone','18612123123')

#修改
stus['name'] = '海龙'

#删除
# del stus['phone']
# stus.pop('phone')
# stus.popitem() #随机删除

#查询

# print(stus['qq'])
# print(stus.get('sex'))

print(stus.keys())
print(stus.values())
stus.update({'moeny':1000})
print(stus)

# for k in stus:
#     print(k,'===>',stus.get(k))

for k,v in stus.items():
    print(k,'===>',v)

# case = {
#     'url':'http://118.24.3.40',
#     'method':'get',
# }

# del stus
#
# print(stus['name'])

'''


#下面是字典嵌套多层取值：


all_stus = {
    'xiaojun':
    {
        'sex': '男',
        'shengao': '185',
        'age': 18,
        'email': 'acb@qq.com',
        'addr': '火星',
        'id': 1,
        'cars':['牧马人','911','野马','劳斯莱斯']
        #五菱宏光
    },
    'hailong':{
        'sex': '男',
        'shengao': '185',
        'age': 18,
        'email': 'acb@qq.com',
        'addr': '火星',
        'id': 2
    },
    'yangfan':{
        'sex': '男',
        'shengao': '185',
        'age': 18,
        'email': 'acb@qq.com',
        'addr': '火星',
        'id': 3,
        'bags':{
            'qianbao':['lv','ysl'],
            'beibao':['coach','abc']
        }
    }
}
all_stus['xiaojun']['cars'].append('五菱宏光')
print(all_stus)
# print(len(all_stus['xiaojun']['cars']))
all_stus['yangfan']['sex'] = '女'
print(all_stus)
all_stus['yangfan']['bags']['qianbao'].remove('lv')


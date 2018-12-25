# json通用的数据类型，所有的语言都认识
# k-v { }
#json串是字符串


s='''
{
        "error_code": 0,
        "stu_info": [
                {
                        "id": 309,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18512572946",
                        "gold": 100
                },
                {
                        "id": 310,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18516572946",
                        "gold": 100
                }
        ]
}

'''
import json



# res = json.loads(s) #json串（字符串），转成字典
# print(res)
# print(res.keys())
# print(type(res))
# #abc,123
# #cba,456
stus = {'xiaojun':'123456','xiaohei':'7891','tanailing':'11111'
        ,'海龙':'111'}
# res2 = json.dumps(stus,indent=8,ensure_ascii=False)
# print(res2)
# with open('stus.json','w',encoding='utf-8') as f:
#     f.write(res2)

# f = open('stus.json',encoding='utf-8')
# content = f.read()
# user_dic = json.loads(content)
# print(user_dic)


# f = open('stus.json',encoding='utf-8')
# user_dic = json.load(f)
# print(user_dic)

stus = {'xiaojun':'123456','xiaohei':'7891','tanailing':'11111'
        ,'海龙':'111'}

res2 = json.dumps(stus,indent=8,ensure_ascii=False)
print(res2)
with open('stus.json','w',encoding='utf-8') as f:
    f.write(res2)


f = open('stus2.json','w',encoding='utf-8')
json.dump(stus,f,indent=4,ensure_ascii=False)

#如果你要把字典写到文件里面的


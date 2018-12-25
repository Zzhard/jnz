# 函数、方法，实现特定功能的一坨代码
# 提高代码的复用性
import json
# with open('a.txt') as f:
#     res = json.load(f)
#
# with open('b.txt') as f:
#     res = json.load(f)
#
# with open('c.txt') as f:
#     res = json.load(f)

def my():
    print('函数')
#函数必须得调用才会执行


#函数里面定义的变量，就是局部变量，局部变量只在函数里面可以使用
#出了函数外面之后，就不能使用了。

def get_file_content(file_name):#形参，形式参数
    #入参：传入一个文件名
    #返回值：文件内容转成字典,返回
    with open(file_name,encoding='utf-8') as f:
        res = json.load(f)
        return res
#一个函数只做一件事
abc = get_file_content('stus.json') #实参，实际参数
# print(abc)
def write_file(filename,content):
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(content,f,ensure_ascii=False,indent=4)
        # f.write(json.dumps(content))

d={'name':'nhy','sex':'nan'}
d2={'aaa':'xxx','a':1}
write_file('nhy.json',d)
write_file('yanfan.json',d2)



#不要把一个函数里面的代码写的特别多

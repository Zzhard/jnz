FILENAME='products.json'
#常量
import json
def get_file_content():
    with open(FILENAME,encoding='utf-8') as f :
        content = f.read()
        if content:
            res = json.loads(content)
        else:
            res = {}
    return res


def write_file_content(dic):
    with open(FILENAME,'w',encoding='utf-8') as fw:
        json.dump(dic,fw,indent=4,ensure_ascii=False)

def check_digit(st:str):
    if st.isdigit():
        st = int(st)
        if st>0:
            return st
    return 0

def add_product():
    product_name = input('请输入商品名称：').strip()
    count = input('请输入商品数量：').strip()
    price = input('请输入商品价格：').strip()
    all_products = get_file_content()
    if check_digit(count) == 0:
        print('数量输入不合法')
    elif check_digit(price) == 0:
        print('价格输入不合法')
    elif product_name in all_products:
        print('商品已经存在')
    else:
        all_products[product_name] = {"count":int(count),
                                      "price":int(price)}
        write_file_content(all_products)
        print('添加成功！')


def show_product():
    product_name = input('请输入要查询的商品名称：').strip()
    all_products = get_file_content()
    if product_name=='all':
        print(all_products)
    elif product_name not in all_products:
        print('商品不存在')
    else:
        print(all_products.get(product_name))



def del_product():
    product_name = input('请输入要删除的商品名称：').strip()
    all_products = get_file_content()
    if product_name in all_products:
        all_products.pop(product_name)
        print('删除成功')
        write_file_content(all_products)
    else:
        print('商品不存在')






choice = input('请输入你的选择:\n 1、添加商品 2、删除商品 3、查看商品信息')
if choice=="1":
    add_product()
elif choice=="2":
    del_product()
elif choice=="3":
    show_product()
else:
    print('输入错误，请重新输入！')
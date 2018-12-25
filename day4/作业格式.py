def add_product():
    pass

def show_product():
    pass

def del_product():
    pass

choice = input('请输入你的选择:\n 1、添加商品 2、删除商品 3、查看商品信息')
if choice=="1":
    add_product()
elif choice=="2":
    del_product()
elif choice=="3":
    show_product()
else:
    print('输入错误，请重新输入！')
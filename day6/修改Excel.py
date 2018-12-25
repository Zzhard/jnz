import xlrd

# from xlutils import copy
# book = xlrd.open_workbook('stu.xls')
# #先用xlrd打开一个Excel
# new_book = copy.copy(book)
# #然后用xlutils里面的copy功能，复制一个Excel
# sheet = new_book.get_sheet(0)#获取sheet页
# sheet.write(0,1,'倪菊芳')
# sheet.write(1,1,'白小军')
# new_book.save('stu.xls')
d = {'喝一瓶': 30, '喝3瓶': 50, '不喝': 1, '买单': 19}


def choice(d):
    print('喝一瓶...')

choice(d)


def export_excel(table_name):
    pass
#user.xls
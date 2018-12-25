import xlrd

book = xlrd.open_workbook('stu.xls')
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name('sheet1')
print(sheet.nrows) #excel里面有多少行
print(sheet.ncols) #excel里面有多少列

print(sheet.cell(0,0).value) #获取到指定单元格的内容
print(sheet.cell(0,1).value) #获取到指定单元格的内容

print(sheet.row_values(0))#获取到整行的内容
# print(sheet.col_values(0))#获取到整行的内容

for i in range(sheet.nrows):#循环获取每行的内容
    print(sheet.row_values(i))
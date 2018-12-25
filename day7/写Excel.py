import xlwt
book = xlwt.Workbook()
sheet = book.add_sheet('xuesheng')
all_data = [
    ['id','name','sex','phone','country'],
    [1,'xiaoming','男',123423432,'china'],
    ['2','xiaoming','男',123423432,'china'],
    ['3','xiaoming','男',123423432,'china'],
    ['4','xiaoming','男',123423432,'china'],
    ['5','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
    ['6','xiaoming','男',123423432,'china'],
]
# line = 0 #行号
# for data in all_data:  #控制行，每次循环行都会变
#     # ['id','name','sex','phone','country']
#     #[1, 'xiaoming', '男', 123423432, 'china'],
#     col = 0  # 列
#     for d in data: #控制列，每次循环lie都会变
#         # id name sex
#         sheet.write(line,col,d)
#         col+=1
#     line+=1

for line,data in enumerate(all_data):
    for col,d in enumerate(data):
        sheet.write(line, col, d)

book.save('s2.xls')


# import string
# case = list(string.ascii_uppercase)
#
# for index,c in enumerate(case):
#     print('%s => %s'%(c,index))

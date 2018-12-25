import xlwt
import xlrd
import xlutils

#写Excel

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
# sheet.write(0,0,'id')#指定行和lie写内容
# sheet.write(0,1,'username')
# sheet.write(0,2,'password')
#
# sheet.write(1,0,'1')
# sheet.write(1,1,'niuhanyang')
# sheet.write(1,2,'123456')

#
stus = [
    [1,'njf','1234'],
    [2,'xiaojun','1234'],
    [3,'hailong','1234'],
    [4,'xiaohei','1234'],
    [4,'xiaohei','1234'],
    [4,'xiaohei','1234'],
    [4,'xiaohei','1234'],
    [4,'xiaohei','1234'],
    [4,'xiaohei','1234'],
]
line = 0 #控制的是行
for stu in stus:#行
    #stu [1,'njf','1234']
    col = 0
    for s in stu:
        #0 0  1
        #0 1 njf
        #0 2 1234

        # 1 0 2
        # 1 1 xiaojun
        # 1 2 1234

        sheet.write(line,col,s)
        col+=1
    line+=1

book.save('stu.xls')# .xlsx



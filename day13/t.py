dic =   {
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2057,
                        "name": "xiaohei",
                        "sex": "nan",
                        "age": 29,
                        "addr": "beijing",
                        "grade": "tianxie",
                        "phone": "18712321234",
                        "gold": 100
                }
        ]
}
import jsonpath
s = jsonpath.jsonpath(dic,'$..error_code')
print(s)

# seqs=['!=','>=','<=','=','<','>','in','notin']
# #list循环这种的话，写用例的时候简单
# s1='error_code=0,name!=xxx,age>18'
# #[error_code>=0 , name!=xxx,age>1]
# s1_list = s1.split(',')
# format_list=[]
# for s in s1_list:
#         #erro_code=0 [error_code,0]
#         #name!=xxx
#         for seq in seqs:
#                 # = != >=
#                 if seq in s:
#                         key,value = s.split(seq)
#                         tmep = [key,seq,value]
#                         format_list.append(tmep)
#                         break
#                         #[[error_code,'=',0] ]
#
# print('format_list',format_list)


#s='erro_code:=:0,name:!=:xxx,age:>:18'
#这种写代码的时候简单

erro_code = 0


# error_code=0
# name!=xxx
# age>18
# < >= in <= notin
#
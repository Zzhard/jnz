import yagmail

user='uitestp4p@163.com'
password='houyafan123'

m = yagmail.SMTP(host='smtp.163.com',user=user,
                 password=password,
                 )
#smtp.qq.com
#smtp_ssl=True 如果是qq邮箱的话加这个参数
m.send(to=['511402865@qq.com','a961813439@163.com'],
       cc=['1336537096@qq.com','13714866626@163.com'],
       subject='明天不上课',contents='明天不上课，在家好好休息。。。',
       attachments=['笔记.txt',r'C:\Users\nhy\Desktop\金牛座.xls'])

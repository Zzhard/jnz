#非空即真，非零即真

name = input('请输入名称：').strip()
#name='abc'
#a=''
#l=[]
#d={}
#t=()
#b=None
name = int(name)
if name:
    print('输入正确')
else:
    print('name不能为空')
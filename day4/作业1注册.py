f = open('users.txt','a+')
f.seek(0)
res = f.read()
all_user_name = [] #存放所有的用户名
for r in res.split('\n'):  # ['username,123456', 'username2,abc123']
    #'username,123456' [username, 123456]
    username = r.split(',')[0]
    all_user_name.append(username)

for i in range(3):
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    cpwd = input('cpwd:').strip()
    if not (len(username)>=6 and len(username)<=20):
    # if len(username)<=6 or len(username)>=20:
        print('用户名长度不合法')
    elif not (len(pwd)>=8 and len(pwd)<=20):
        print('密码长度不合法')
    elif pwd!=cpwd:
        print('两次输入的密码不一致')
    elif username in all_user_name:
        print('用户名已经被注册')
    else:
        user_info = '%s,%s\n'%(username,pwd)
        f.write(user_info)
        print('注册成功！')
        break
else:
    print('错误次数过多')
f.close()
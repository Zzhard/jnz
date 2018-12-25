

# usename,123456
all_user = {}
res = open('users.txt').read()
for r in res.split('\n'):  # ['username,123456', 'username2,abc123']
    #'username,123456' [username, 123456]
    if r.strip()!='':
        username = r.split(',')[0]
        pwd = r.split(',')[1]
        all_user[username] = pwd
for i in range(3):
    username = input('username:')
    pwd = input('pwd:')
    if username in all_user:
        if pwd == all_user.get(username):
            print('欢迎登陆！')
        else:
            print('账号/密码错误！')
    else:
        print('该用户未注册！')


# username = input('username:')
# pwd = input('pwd:')
# user_info= username+','+pwd
# # usename,123456
# if user_info in res:
#     print('登陆成功！')
# else:
#     print('登陆失败，账号、密码错误')
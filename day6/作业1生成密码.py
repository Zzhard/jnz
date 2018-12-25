import random
import string

def gen_password1():
    pwd_len = random.randint(8,16)
    upper = random.sample(string.ascii_uppercase,1)
    lower = random.sample(string.ascii_lowercase,1)
    digit = random.sample(string.digits,1)
    punctuation = random.sample(string.punctuation,1)
    other = random.sample(string.ascii_letters+string.digits+string.punctuation
                  ,pwd_len-4)
    res = upper+lower+digit+punctuation+other
    random.shuffle(res)
    return ''.join(res)

def gen_password2():
    pwd_len = random.randint(8,16)
    all_str = string.ascii_letters+string.digits+string.punctuation
    res = set(random.sample(all_str,pwd_len))
    if res & set(string.ascii_lowercase) and res & set(string.digits) \
         and res & set(string.ascii_uppercase) and res & set(string.punctuation):
        return ''.join(res)
    return gen_password2()



all_passwords=set()
num = int(input('请输入要产生多少条密码:').strip())
while len(all_passwords) != num:
    # res = gen_password1()+'\n'
    res = gen_password2()+'\n'
    #xbA17\n
    all_passwords.add(res)
with open('passwords.txt','w',encoding='utf-8') as fw:
    fw.writelines(all_passwords)








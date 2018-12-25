# res = ['01','02','03','33']
# res = []
# for i in range(1,34):
#     res.append(str(i).zfill(2))

# res = [ str(i).zfill(2) for i in range(1,34)]
# l = [  i  for i in range(10) ]
# print(l)
# print(res)
import random
all_red_ball = [str(i).zfill(2) for i in range(1, 34)]
all_blue_ball = [str(i).zfill(2) for i in range(1, 17)]
def gen_seq():
    blue = random.choice(all_blue_ball)
    red = random.sample(all_red_ball,6)
    red = ' '.join(red)
    return '红球:%s 篮球:%s'%(red,blue)
all_seq=set()
num = int(input('请输入要产生多少条双色球:').strip())
while len(all_seq) != num:
    # res = gen_password1()+'\n'
    res = gen_seq()+'\n'
    #xbA17\n
    all_seq.add(res)
with open('passwords.txt','w',encoding='utf-8') as fw:
    fw.writelines(all_seq)

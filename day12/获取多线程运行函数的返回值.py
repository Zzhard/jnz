import requests
import threading

all_res = []
def get_name(name):
    r = requests.get('http://api.nnzhp.cn/api/user/stu_info',
                     params={'stu_name':name})
    res = r.json()
    all_res.append(res)

for i in range(10):
    t = threading.Thread(target=get_name,args=(i,))
    t.start()

while threading.active_count()!=1:
    pass

print(all_res)
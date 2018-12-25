from urllib.request import urlopen
from urllib.parse import urlencode
url='http://www.nnzhp.cn/archives/423'

# res=urlopen(url).read()  #发送get请求
# print(res.decode())
# f = open('a.html','w',encoding='utf-8')
# f.write(res.decode())
# f.close()

url='http://api.nnzhp.cn/api/user/login'
data = {"username":"niuhanyang","passwd":'aA123456'}
data = urlencode(data)
res = urlopen(url,data.encode()).read()
print(res.decode())
import json
d = json.loads(res.decode())
print(d.get('login_info').get('sign'))
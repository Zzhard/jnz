import requests
import time
import threading
def download_html(url,file_name):
    res = requests.get(url)
    with open(file_name+'.html','wb') as fw:
        fw.write(res.content)
    print('【%s】下载完成'%file_name)

urls={
    'nnzhp':'http://www.nnzhp.cn',
    'cc':'http://www.cc-na.cn',
    'dsx':'http://www.imdsx.cn',
    'besttest':'http://www.besttest.cn',
}

start_time = time.time()

for file_name,url in urls.items():
    t = threading.Thread(target=download_html,args=(url,file_name))
    #args=(url,) #单个参数的时候，一定要这么写
    t.start()
while threading.active_count()!=1:
    pass

end_time = time.time()
print('run time =',end_time - start_time)

    #单线程
# start_time = time.time()
# for k,v in urls.items():
#     download_html(url=v,file_name=k)
# end_time = time.time()
# print('run time =',end_time - start_time)


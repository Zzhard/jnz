import threading
import time
def run():
    time.sleep(5)
    print('over')

start_time = time.time()
for i in range(100):
    t = threading.Thread(target=run)
    t.start()

print('运行的时候几个线程',threading.activeCount() ) # 1
#threading.activeCount就是当前有几个线程
while 1:
    if threading.active_count()==1:
        break


print('这时候几个线程',threading.activeCount()) # 2
end_time = time.time()
print('run time =',end_time - start_time) #

print('运行结束')


''' 第一种for循环主线程等待子线程运行结束
start_time = time.time()
ths = [] #100
for i in range(100):
    t = threading.Thread(target=run) #实例化一个线程，
    t.start()#启动这个线程
    ths.append(t)

for t in ths:
     t.join() #循环等待每个子线程执行结束
end_time = time.time()
print('run time =',end_time - start_time)
'''

    # start_time = time.time()
# run()
# run()
# run()
# run()
# end_time = time.time()
# print('run time =',end_time - start_time)
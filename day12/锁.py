#coding=utf-8
import threading
num = 0
lock = threading.Lock()  #申请一把锁
def xiaojun():
    global num
    # lock.acquire() #加锁
    # num+=1
    # lock.release() #解锁
    # with lock: #和上面一样
    #     num += 1
    num +=1
for i in range(1000):
    t = threading.Thread(target=xiaojun)
    t.start()
while threading.active_count()!=1:
    pass
print(num)
#多个线程同时操作同一个数据的时候一定要加锁
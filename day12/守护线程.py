import threading
import time


def hhh():
    time.sleep(5)
    print('hhhh')

for i in range(100):
    t = threading.Thread(target=hhh)
    t.setDaemon(True) #设置子线程为守护线程
    t.start()

print('秦始皇死了')

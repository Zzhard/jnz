from multiprocessing import Process
import multiprocessing
import time
import threading
def run_thread():
    time.sleep(60)
    print('%s在运行'%threading.current_thread())


def run():
    for i in range(10):
        t = threading.Thread(target=run_thread)
        t.start()
    while threading.active_count()!=1:
        pass

for i in range(10):
    p = Process(target=run) #起进程
    p.start()
    p.pid

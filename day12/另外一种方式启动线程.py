import threading
import time

class MyThread(threading.Thread):
    def run(self):
        #这个方法必须叫run
        time.sleep(5)
        print('run..')


for i in range(5):
    t = MyThread()
    t.start()
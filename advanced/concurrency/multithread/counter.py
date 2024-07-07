from threading import Thread, Lock
import time
import random

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.count += 1
            
    def increment(self):
        self.lock.acquire()  # 手动获取锁
        try:
            self.count += 1
        finally:
            self.lock.release()  # 无论如何都确保释放锁

 
def worker(counter):
    for _ in range(10000):
        counter.increment()

for _ in range(50):  # 运行5次
    counter = SafeCounter()
    threads = []

    for _ in range(10):
        t = Thread(target=worker, args=(counter,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Final count: {counter.count}")

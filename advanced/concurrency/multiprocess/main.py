import os

print(os.cpu_count()) #在本文件中，这行会执行3次，分别在主进程和两个子进程中执行


import time
from multiprocessing import Process, Queue

def sub_task(content, queue):
    counter = queue.get()
    while counter < 5:
        print(content, end='', flush=True)
        counter += 1
        queue.put(counter)
        time.sleep(0.01)
        counter = queue.get()

def main():
    queue = Queue()
    queue.put(0)
    p1 = Process(target=sub_task, args=('Ping', queue))
    p1.start()
    p2 = Process(target=sub_task, args=('Pong', queue))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    queue.put(5) # 用于退出子进程的循环


if __name__ == '__main__':
    main()
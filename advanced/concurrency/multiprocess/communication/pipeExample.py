from multiprocessing import Process, Pipe
import os
import time
import random

'''
这段代码展示了如何在Python中使用多进程和管道（Pipe）进行进程间通信。
代码的主要目的是创建五个工作进程（worker），每个进程通过管道接收消息，处理消息，然后在接收到特定的停止信号（'STOP'）后退出。
'''
def worker(pipe_end, name):
    print(f"Process {name} (PID: {os.getpid()}) started.")
    while True:
        msg = pipe_end.recv()
        if msg == 'STOP':
            print(f"Process {name} received STOP signal. Exiting...")
            break
        num = random.randint(1, 3)
        time.sleep(num)  # 模拟处理消息的耗时操作
        print(f"Process {name} received message: {msg}")
    pipe_end.close()


if __name__ == '__main__': 
    # Start 5 worker processes
    processes = []
    parent_conns = {}
    for i in range(5):
        # Create pipes
        parent_conn, child_conn = Pipe() # pipe的两个connection都可以发送和接收消息
        p = Process(target=worker, args=(child_conn, f"Worker-{i}"))
        processes.append(p)
        parent_conns[p] = parent_conn
        p.start()
    
    # Send messages to processes
    # 发送消息给每个子进程
    for i, process in enumerate(processes):
        parent_conn = parent_conns[process]
        parent_conn.send(f"Message {i}")  # 这里需要修改逻辑，确保消息发送给正确的子进程
       
    # Send stop signal to all processes
    for i, process in enumerate(processes):
        parent_conn = parent_conns[process]
        parent_conn.send('STOP')
    
    # Wait for all processes to finish
    for p in processes:
        p.join()
    
    print("All processes finished.")

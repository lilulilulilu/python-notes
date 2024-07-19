from multiprocessing import Process, Manager
import os
'''
multiprocessing.Manager() 提供的服务进程可以创建多种类型的共享数据结构，以便在多个进程之间进行共享和通信。
这些共享数据结构包括但不限于：
    list: 一个可以在多个进程间共享的列表。
    dict: 一个可以在多个进程间共享的字典。
    Namespace: 一个简单的对象，其属性可以在多个进程间共享。
    Value: 用于存储一个单一的值，可以是 ctypes 类型，如 ctypes.c_double。
    Array: 类似于 Value，但用于存储一个数组，其元素类型可以是 ctypes 类型。
    Queue: 一个进程安全的队列，用于跨进程通信。
    Event: 一个进程间同步原语，可以用来通知多个进程某个事件的发生。
    Lock: 一个基本的进程间互斥锁。
    RLock: 一个可重入的互斥锁，允许在同一进程中多次获得，但必须释放相同的次数以解锁。
    Semaphore: 一个进程间信号量。
    Condition: 一个进程间条件变量，允许一个或多个进程等待某个条件成立。
    这些数据结构通过 Manager() 创建的实例进行访问和操作，它们被设计为可以安全地在多个进程之间共享和修改。
    使用这些共享数据结构可以帮助实现进程间的通信和数据共享，是多进程编程中的重要工具。
'''

def modify_list(shared_list):
    shared_list.append(f'I am {os.getpid()}')

if __name__ == '__main__':
    with Manager() as manager:
        shared_list = manager.list()  # 创建一个共享的列表
        # 创建多个进程，每个进程都向共享列表中添加一个唯一的元素
        processes = [Process(target=modify_list, args=(shared_list,)) for _ in range(3)]
        for p in processes: # 启动所有进程
            p.start()
        for p in processes: # 等待所有进程结束
            p.join()

        print(shared_list)  # 输出修改后的列表,['I am 25986', 'I am 25987', 'I am 25988']。这行必须在with body内，否则会报错
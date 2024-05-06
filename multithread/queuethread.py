import threading
import queue
import time

def producer(queue):
    for i in range(5):
        item = f'数据{i}'
        queue.put(item)
        print(f'生产者产生了: {item}')
        # time.sleep(1)  # 模拟耗时的生产过程

def consumer(queue):
    while True:
        item = queue.get()
        print("item:",item)
        if item is None:
            break  # None是结束信号
        print(f'消费者消费了: {item}')
        queue.task_done()

# 创建队列
q = queue.Queue()

# 创建并启动生产者和消费者线程
producerT = threading.Thread(target=producer, args=(q,))
consumerT = threading.Thread(target=consumer, args=(q,))
producerT.start()
consumerT.start()

# 等待生产者线程结束
producerT.join()

# 发送结束信号给消费者
q.put(None)

# 等待消费者线程结束
consumerT.join()
print("all is done")

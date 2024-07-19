from multiprocessing import Process, Queue
import time

def worker(input_queue, id):
    while True:
        msg = input_queue.get()  # 从队列中获取消息
        if msg == "STOP":
            print(f"Process {id} stopping.")
            break
        print(f"Process {id} received message: {msg}")
        # 可以在这里处理消息，并将结果放回队列（如果需要）

if __name__ == "__main__":
    queue = Queue()  # 创建一个队列

    # 创建并启动5个工作进程
    processes = [Process(target=worker, args=(queue, i)) for i in range(5)]
    for p in processes:
        p.start()

    # 向队列中发送消息
    for i in range(10):
        queue.put(f"Message {i}")
        time.sleep(1)  # 等待一段时间，以便观察输出

    # 发送停止信号
    for _ in range(5):
        queue.put("STOP")

    # 等待所有进程完成
    for p in processes:
        p.join()

    print("All processes finished.")
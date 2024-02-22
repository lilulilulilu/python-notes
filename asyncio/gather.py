'''
在这个例子中，asyncio.run(main()) 是启动 asyncio 程序的入口点。
main 协程内，我们使用 asyncio.gather 来并发运行 task1 和 task2。
因为这两个任务都包含 await asyncio.sleep(...) 调用，这模拟了异步 I/O 操作，让出控制权给事件循环，允许其他任务运行。
task2 会首先完成，因为它等待的时间少于 task1。

asyncio 的强大之处在于它提供了一种方式来编写并发代码，这种代码在写法上与同步代码相似，但执行上却可以处理数百甚至数千的并发连接，这对于高性能网络服务器和相关应用非常有用。
'''

import asyncio
import time

def current_time():
    return time.asctime(time.localtime(time.time()))

async def task1():
    print(f'{current_time()} - Task 1 start')
    await asyncio.sleep(2)  # 模拟 I/O 操作，比如网络请求
    print(f'{current_time()} - Task 1 done')

async def task2():
    print(f'{current_time()} - Task 2 start')
    await asyncio.sleep(1)  # 模拟 I/O 操作
    print(f'{current_time()} - Task 2 done')

async def main():
    # 同时运行两个任务，直到它们全部完成
    await asyncio.gather(task1(), task2())
    

# 运行主协程
asyncio.run(main())

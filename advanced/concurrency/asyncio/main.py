# https://docs.python.org/zh-cn/3.12/library/asyncio.html#module-asyncio

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def reply_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}s"
 
 
'''
示例一：顺序执行，总耗时3秒
以下代码段会在等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world"
'''
async def main():
    print(f"start at {time.strftime('%X')}") 
    await say_after(1, "hello")
    await say_after(2, "world") 
    print(f"end at {time.strftime('%X')}")
    
'''
示例二：asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
main2将并发运行两个 say_after 协程，总耗时2s
'''
async def main2(): 
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world")) 
    print(f"start at {time.strftime('%X')}") 
    await task1
    await task2
    print(f"end at {time.strftime('%X')}")

    
'''
示例三：同示例二，但是带返回值
'''
async def main3(): 
    task1 = asyncio.create_task(reply_after(1, "hello"))
    task2 = asyncio.create_task(reply_after(2, "world")) 
    print(f"start at {time.strftime('%X')}") 
    result1 = await task1
    result2 = await task2
    print(f"end at {time.strftime('%X')}, result1:{result1}, result2:{result2}")

   
if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
    asyncio.run(main3())
    

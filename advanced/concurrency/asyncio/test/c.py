import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    start = asyncio.get_running_loop().time()
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    task3 = asyncio.create_task(say_after(3, "python"))
    
    await task1
    await task2
    await task3
    end = asyncio.get_running_loop().time()
    print("Finished in total seconds:", end - start)


asyncio.run(main())
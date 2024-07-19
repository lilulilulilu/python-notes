import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial 
from typing import List
from timeit import async_timed
import time

def count (count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter = counter + 1 
    print(counter)    
    return counter


@async_timed()
async def main ():
    '''
    in this main, we use ProcessPoolExecutor to run the count function in a separate process.
    and we use asyncio.get_running_loop to get the current running loop.
    and we use loop.run_in_executor to run the count function in the ProcessPoolExecutor.
    and we use asyncio.gather to wait for all the count functions to finish.
    '''
    with ProcessPoolExecutor () as pool:
        loop = asyncio.get_running_loop() 
        nums = [1, 3, 5, 22, 100000000]
        calls = [partial(count, num) for num in nums] # 使用其参数为倒计时创建一个偏应用的函数。 
        futures = []
        
        # add each partial function to the event loop
        for call in calls:
            # 这行代码的作用是在asyncio程序中安排一个阻塞操作call在指定的执行器pool中异步执行，
            # 这个pool可以是一个线程池（ThreadPoolExecutor），也可以是一个进程池（ProcessPoolExecutor）。
            # 并通过Future对象future_object来跟踪这个操作的完成情况和结果。
            # 这样做可以将阻塞操作从事件循环中分离出来，提高程序的响应性和性能。 
            future_object = loop.run_in_executor(pool, call) 
            futures.append(future_object) # 添加到futures列表中，便于后续加入gather变成任务被eventloop调度执行。
        
        print("futures created, but did not run yet")
        start = time.time()
        results = await asyncio.gather(*futures)  # run all the futures in the event loop
        end = time.time()
        print(f'Finished in total seconds: {end - start}, results: {results}')

if __name__ == "__main__": 
    asyncio.run(main())
    
'''
loop.run_in_executor is a function of the asyncio module, it is used to run a function in a executor (a separate thread or process).
this function will return a Future object, which can be awaited to get the result of the function.

'''
import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial 
from typing import List
from timeit import async_timed

def count (count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter = counter + 1 
    return counter

@async_timed()
async def main ():
    with ProcessPoolExecutor () as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop() 
        nums = [1, 3, 5, 22, 100000000]
        calls: List [partial[int]] = [partial (count, num) for num in nums] # 使用其参数为倒计时创建一个偏应用的函数。 
        call_coros = []
        # 将每个调用提交到进程池，并将其附加到列表中。
        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call)) # 在指定的执行器process_pool中调用call 。
            
        results = await asyncio.gather(*call_coros) 
        for result in results:
            print(result)

if __name__ == "__main__": 
    asyncio.run(main())
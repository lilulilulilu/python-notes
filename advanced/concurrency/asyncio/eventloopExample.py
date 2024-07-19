import asyncio
import time
'''
创建一个事件循环,让它接收一个协程,并运行任务直到完成
'''

async def delay(seconds: int):
    await asyncio.sleep(1)
    print(f"I'm finished in {seconds} seconds")
    
def main1():
    start = time.time()
    loop = asyncio.new_event_loop() #创建一个事件循环
    coro1 = delay(1) #创建一个协程
    coro2 = delay(2)
    coro3 = delay(3)
    try:
        # 接收一批协程，并运行它直到完成
        loop.run_until_complete(coro1)  
        loop.run_until_complete(coro2)  
        loop.run_until_complete(coro3)  
        end = time.time()
    finally:
        loop.close()
    print("Finished in total seconds:", end - start)

main1()   
    
# def call_later () :
#     print ("I'm being called in the future!")
    
# async def main():
#     loop = asyncio.get_running_loop() 
#     loop.call_soon(call_later) #在事件循环的下一次迭代中运行call_later
#     await delay(1)
    
# asyncio.run(main())
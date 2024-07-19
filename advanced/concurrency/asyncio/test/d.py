import asyncio

'''
创建一个事件循环,让它接收一组协程,并行的运行这批任务，直到所有任务完成
'''

async def delay(seconds: int):
    await asyncio.sleep(1)
    
def main1():
    loop = asyncio.new_event_loop() #创建一个事件循环
    asyncio.set_event_loop(loop) #设置为当前事件循环
    
    start = asyncio.get_event_loop().time() 

    coro1 = delay(1) #创建一个协程
    coro2 = delay(2)
    coro3 = delay(3)
    try:
        # 接收一个协程，并运行它直到完成
        loop.run_until_complete(coro1)  
        loop.run_until_complete(coro2)  
        loop.run_until_complete(coro3)  
        end = asyncio.get_event_loop().time() 
    finally:
        loop.close()
    
    print("Finished in total seconds:", end - start)


main1()

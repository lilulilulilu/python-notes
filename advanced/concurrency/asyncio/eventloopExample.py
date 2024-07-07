import asyncio

'''
创建一个事件循环,让它接收一个协程,并运行任务直到完成
'''

async def delay(seconds: int):
    await asyncio.sleep(1)
    
def main1():   
    loop = asyncio.new_event_loop() #创建一个事件循环
    delay_coro = delay(1) #创建一个协程
    try:
        loop.run_until_complete(delay_coro)  # 接收一个协程，并运行它直到完成
    finally:
        loop.close()
    
    
def call_later () :
    print ("I'm being called in the future!")
    
async def main():
    loop = asyncio.get_running_loop() 
    loop.call_soon(call_later) #在事件循环的下一次迭代中运行call_later
    await delay(1)
    
asyncio.run(main())
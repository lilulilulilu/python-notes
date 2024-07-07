from asyncio import Future 
import asyncio

async def set_future_value(future) -> None:
    await asyncio.sleep(1) # 设置future值之前等待1秒
    future.set_result(42) # 设置future的值为42
    
def make_request () -> Future: 
    future = Future()
    set_future_value_coro = set_future_value(future) #创建一个协程来异步设置future的值
    asyncio.create_task(set_future_value_coro) #创建一个任务来异步设置future的值
    return future
    
async def main () :
    future = make_request()
    print(f'Is the future done? {future.done()}') 
    value = await future  #暂停main,直到 future 的值被设置完成。
    print(f'Is the future done? {future.done()}') 
    print(value)
        
asyncio.run(main())
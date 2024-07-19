import asyncio

async def say_after(delay: int, what: str) -> None :
    await asyncio.sleep(delay)  # 使用 delay 参数
    print ("I'm being called in the future!")
    
async def main():
    loop = asyncio.get_running_loop() 
    loop.call_soon(say_after,(1,"hello") )#在事件循环的下一次迭代中运行call_later
    
asyncio.run(main())
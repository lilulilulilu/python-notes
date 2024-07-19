import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    print("Started")
    start = asyncio.get_event_loop().time()
    
    await asyncio.gather(
        say_after(1, "hello"),
        say_after(2, "world"),
        say_after(3, "python")
    )
    
    end = asyncio.get_event_loop().time()
    print("Finished cost time:", end - start)
    
asyncio.run(main())


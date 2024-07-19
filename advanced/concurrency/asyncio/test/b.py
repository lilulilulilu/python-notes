import asyncio

    
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    coro1 = say_after(1, "hello") # actually it's not a task, it's a coroutine object
    coro2 = say_after(2, "word")
    coro3 = say_after(3, "python")
    
    start = asyncio.get_event_loop().time()

    tasks = []
    task1 = asyncio.create_task(coro1) # create a task from a coroutine object, now it's a task and it will be scheduled by the event loop.
    task2 = asyncio.create_task(coro2)
    task3 = asyncio.create_task(coro3)
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    '''
    event loop will schedule the task1, task2, task3 to run concurrently,
    
    '''
    
    for task in tasks:
        await task

    end = asyncio.get_event_loop().time()
    print("Finished in total seconds:", end - start)
    
asyncio.run(main()) # create a event loop and run the coroutine main() in the event loop
import asyncio

async def task1():
    await asyncio.sleep(1)
    raise ValueError("任务1出错了")

async def task2():
    await asyncio.sleep(2)
    return "任务2完成"

'''
return_exceptions=True可以防止某个任务出异常影响到gather中的其他任务。
'''
async def main():
    results = await asyncio.gather(task1(), task2(), return_exceptions=True)
    for result in results:
        if isinstance(result, Exception):
            print(f"任务出错: {result}")
        else:
            print(f"任务结果: {result}")

asyncio.run(main())


'''
python gather_exception.py 执行结果：
任务出错: 任务1出错了
任务结果: 任务2完成
'''
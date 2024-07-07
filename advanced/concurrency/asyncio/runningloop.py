import asyncio

'''
读取事件循环对象，并给时间循环安排一个任务
'''


async def some_coro():
    print("Running some task")
    
    
async def main():
    # 获取当前正在运行的事件循环
    loop = asyncio.get_running_loop()

    # 打印事件循环对象
    print(loop) # <_UnixSelectorEventLoop running=True closed=False debug=False>

    # 在事件循环中安排一个任务
    loop.create_task(some_coro())


# 运行主函数
asyncio.run(main())
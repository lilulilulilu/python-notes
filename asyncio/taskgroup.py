'''
从 Python 3.11 开始，asyncio 引入了一个新的特性：TaskGroup。
TaskGroup 提供了一种结构化的方式来同时运行和管理多个异步任务。
与 asyncio.gather() 相比，TaskGroup 提供了更好的异常处理和任务取消机制。
使用 TaskGroup，当组内的任何任务失败时（抛出异常），所有其他任务将自动取消，且相关的异常会被抛出到 TaskGroup 的上下文管理器外。
TaskGroup 提供了针对调度嵌套子任务的比 gather 更强的安全保证：如果一个任务（或子任务，即由一个任务调度的任务）引发了异常，TaskGroup 将取消剩余的已排期任务）。
使用 TaskGroup 的好处是它提供了更加结构化和安全的方式来并发运行和管理多个异步任务。通过自动处理任务取消和异常传播，TaskGroup 使得并发代码的编写更加简洁和可靠。
'''

import asyncio

async def task1():
    await asyncio.sleep(1)
    print("任务1完成")
    return "结果1"

async def task2():
    await asyncio.sleep(2)
    print("任务2完成")
    return "结果2"

async def task3():
    await asyncio.sleep(1)
    raise ValueError("任务3出现错误")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
        tg.create_task(task3()) # task33()抛出异常, TaskGroup会自动取消所有其他任务

try:
    asyncio.run(main())
except ValueError as e:
    print(f"捕获异常: {e}")

'''
在这个示例中，main() 函数中创建了一个 asyncio.TaskGroup 实例，并通过 async with 语句管理其生命周期。在 TaskGroup 的上下文管理器内，我们使用 tg.create_task() 方法添加三个异步任务。如果这些任务中的任何一个抛出异常（如 task3() 所做），则 TaskGroup 会自动取消所有其他正在运行的任务，并将异常抛出到 async with 语句的外部。在这个例子中，异常被捕获并处理。
'''
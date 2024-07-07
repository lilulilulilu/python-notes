import asyncio

# 定义一个协程函数
async def hello():
    print("Hello, World!")
    await asyncio.sleep(1)  # 使用await关键字等待一个协程
    return "Hello, World!"

# 模拟异步I/O操作
async def download(url):
    print(f"Start downloading {url}")
    await asyncio.sleep(1)  # 模拟异步I/O操作
    print(f"Finish downloading {url}")
    return url

# 新增一个协程函数
async def goodbye():
    print("Goodbye, World!")
    await asyncio.sleep(1)
    return "Goodbye, World!"

# 主协程
async def main():
    # 在事件循环中创建一个任务
    task = asyncio.create_task(hello())  # 创建一个任务
    result = await task  # 等待任务完成并获取返回值
    print(f"hello result: {result}")

    # 运行下载函数
    result = await download("http://example.com")
    print(f"download result: {result}")

    # 使用gather并发运行多个协程，并收集他们的结果
    results = await asyncio.gather(goodbye(), download("http://example.com"))
    print(f"gather results: {results}")

# 创建一个事件循环，并在这个事件循环中运行主协程
asyncio.run(main())
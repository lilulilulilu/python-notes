import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def aggregate_transactions():
    # 连接到 MongoDB 数据库
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    database = client['mydatabase']  # 替换为你的数据库名
    collection = database['orders']  # 替换为你的集合名

    # 定义聚合管道
    pipeline = [
        {'$match': {'size': 'small'}},  # 筛选条件，仅考虑完成的交易
        {'$sort': {'price': 1}}     # 结果按 price 升序排序
    ]

    # 执行聚合查询
    async for document in collection.aggregate(pipeline):
        print(document)

    # 关闭数据库连接
    client.close()

# 运行异步事件循环
asyncio.run(aggregate_transactions())

import motor.motor_asyncio
import asyncio

async def main():
    # 创建MongoDB客户端，配置连接池参数
    client = motor.motor_asyncio.AsyncIOMotorClient(
        'mongodb://localhost:27017',
        maxPoolSize=20,  # 最大连接数
        minPoolSize=5   # 最小连接数
    )

    # 指定数据库
    db = client['mydatabase']

    # 指定collection
    collection = db['mycollection']

    # 插入一个文档作为示例
    document = {'name': 'Bob', 'age': 30}
    result = await collection.insert_one(document)
    print('Inserted document:', result.inserted_id)

    # 关闭客户端（在实际应用中通常不需要手动关闭，除非特定情况）
    client.close()

# 使用asyncio运行异步main函数
asyncio.run(main())

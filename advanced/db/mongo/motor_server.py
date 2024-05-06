from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

import uvicorn
app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# 创建MongoDB客户端
client = AsyncIOMotorClient(
    'mongodb://admin:mongo666@localhost:27017/admin',
    maxPoolSize=20,  # 最大连接数
    minPoolSize=5   # 最小连接数
)
db = client['mydatabase']
collection = db['mycollection']


@app.post("/insert/")
async def insert_user(user: User):
    result = await collection.insert_one(user.dict())
    return {"inserted_id": str(result.inserted_id)}

@app.get("/")
def read_root():
    return "hello world"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000)
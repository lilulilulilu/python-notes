
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from typing import List
from pydantic import BaseModel

import uvicorn

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('DMetaSoul/Dmeta-embedding')

app = FastAPI()

class RequestBody(BaseModel):
    content: str
    id: str
    
class ResponseBody(BaseModel):
    content: str
    id: str
    content_embedding: List[float]



def get_embedding(texts: str, model) -> List:
    embedding = model.encode(texts, normalize_embeddings=True)
    return embedding


@app.post("/embedding/")
def read_item(item: RequestBody):


    content = item.content
    id = item.id
    
    texts = [content]
    embedding_list = get_embedding(texts, model)
    print("embedding_list:", embedding_list)
    print("embedding_list[0]:", embedding_list[0].tolist())

    ret = ResponseBody(
        content=content,
        id=id,
        content_embedding=embedding_list[0].tolist()
    )
    
    return ret
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8880)

# CUDA_VISIBLE_DEVICES=7 nohup python embedding_server.py > log.log 2>&1 &
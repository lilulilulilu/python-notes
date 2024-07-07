from transformers import AutoTokenizer
from transformers import LlamaForCausalLM
import torch
import string


device = torch.device("cuda")
modelpath = "IDEA-CCNL/Ziya-LLaMA-13B-v1"
model = LlamaForCausalLM.from_pretrained(modelpath, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(modelpath)

import uvicorn
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryBoby(BaseModel):
    query: str
    
class ResponseBoby(BaseModel):
    answer: str
    

@app.post("/generate")
async def generate(body: QueryBoby):
    query = body.query
    inputs = query
    input_ids = tokenizer(inputs, return_tensors="pt").input_ids.to(device)
    generate_ids = model.generate(
                input_ids,
                max_new_tokens=4096, 
                do_sample = True, 
                top_p = 1, 
                temperature = 1.0, 
                repetition_penalty=1., 
                eos_token_id=2, 
                bos_token_id=1, 
                pad_token_id=0)
    output = tokenizer.batch_decode(generate_ids)[0]
    start = len('<s>\n')+len(inputs)
    answer = output[start: -4]
    return ResponseBoby(answer=answer)



if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=6000)
   

      


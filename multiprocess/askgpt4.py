from openai import OpenAI
client = OpenAI(api_key="sk-ssssssssssssss")

import json
from tqdm import tqdm
import multiprocessing
import os


def askgpt4(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

'''
处理函数
start, end:起点行数和终点行数 
lines: 所有行
output_file: 结果保存文件名
func: 处理函数
'''
def process_lines(start, end, lines, output_file, func):
    # 仅处理分配的行
    with open(output_file, 'a', encoding='utf-8') as outfile:
        for i in range(start, min(end, len(lines))):
            json_obj = json.loads(lines[i].strip())
            try:
                prompt = json_obj['prompt']
                answer = func(prompt)
                json_obj['answer'] = answer
                json.dump(json_obj, outfile, ensure_ascii=False)
                outfile.write("\n")
                outfile.flush()
            except Exception as e:
                print("error prompt:\n",json_obj['prompt'])
                print(f"Error processing line: {e}")
    print(f'{output_file} finished.')

'''
将数据分批，每批数据创建一个进程，调用处理函数处理。
默认情况是每10行为一批数据
存到results目录下
每行数据会使用到func函数
'''
def read_and_ask_parallel(file_path, output_dir="results", chunk_size=10, func=askgpt4):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 每个进程处理的行数
    processes = []
    for i in range(0, len(lines), chunk_size):
        output_file = f'{output_dir}/output_process_{i//chunk_size}.json'
        # 检查文件是否存在，如果存在，则删除
        if os.path.exists(output_file):
            os.remove(output_file)
        
        process = multiprocessing.Process(target=process_lines, args=(i, i+chunk_size, lines, output_file, func))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

if __name__ == '__main__':   
    # prompts.jsonl中每行数据都是一个{"prompt":"xxxxx"}的json数据
    read_and_ask_parallel('prompts.jsonl', chunk_size = 10)
           


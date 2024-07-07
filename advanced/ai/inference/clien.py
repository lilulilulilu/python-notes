import requests
import string
from datetime import datetime


systemprompt = '''下面是一段对话，请续写对话。
$conversation'''

systemprompt_template = string.Template(systemprompt)

def now_time() -> str:
    """ 获取当前时间，格式化为字符串，包含星期几 """
    currentDateAndTime = datetime.now()
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday_num = currentDateAndTime.weekday()
    weekday = weekdays[weekday_num]
    currentTime = currentDateAndTime.strftime("%Y-%m-%d %H:%M:%S")
    ymd, hms = currentTime.split(' ')
    currentTime = ' '.join([ymd, weekday, hms])
    return currentTime

history = ""
    
def format_query(query):
    now = now_time()
    conversation = f'{history}<A>[{now}]:{query.strip()}\n<B>[{now}]:'
    prompt = systemprompt_template.substitute({"conversation":conversation})
    return prompt, conversation

def chat(prompt):
    url = "http://ip:port/generate"
    body = {
        "query": prompt
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, json=body, headers=headers)
    return response.json()['answer']

if __name__ == "__main__":
    
    queries = ["你好", "你会做什么？"]
    
    for query in queries:
        prompt, conversation = format_query(query)
        answer = chat(prompt)
        print(f'conversation:\n{conversation}\nanswer:{answer}\n')
        print("------------------------------------")
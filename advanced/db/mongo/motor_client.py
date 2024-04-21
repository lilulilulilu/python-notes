import requests

def create_user(name, age):
    url = 'http://127.0.0.1:6000/insert/'
    data = {'name': name, 'age': age}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    # 测试创建用户
    user_info = create_user("mary", 30)
    print("Response from server:", user_info)

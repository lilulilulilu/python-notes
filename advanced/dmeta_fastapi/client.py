import requests
import json

def test_embedding_api():
    url = 'http://localhost:8880/embedding/'
    headers = {'Content-Type': 'application/json'}
    data = {
        'content': 'Test content of the document.',
        'id': '12345'
    }
    
    # 发送POST请求
    response = requests.post(url, headers=headers, json=data)
    
    # 确保请求成功
    print("statuscode:", response.status_code)
    assert response.status_code == 200
    
    # 加载响应数据
    response_data = response.json()
    print(response_data)
    
    # 验证响应数据包含所有必要的键
    expected_keys = { 'content', 'id', 'content_embedding'}
    assert set(response_data.keys()) == expected_keys
    
    # 进一步的验证可以包括检查嵌入向量的具体值，但这取决于get_embedding函数的实现细节
    print("Test passed!")

# 运行测试用例
if __name__ == "__main__":
    test_embedding_api()


# 一次性读取所以内容，返回一个字符串数组，数组中一个元素就是一行
def get_lines():
    with open('text.txt','r') as f:
        return f.readlines()

def get_lines2():
    with open('text.txt','rb') as f:
        for i in f:
            yield i

if __name__ == '__main__':
    for e in get_lines2():
        print(e.strip()) # strip()去掉首尾空格或换行符
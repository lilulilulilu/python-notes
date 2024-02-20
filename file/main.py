from functools import partial
'''
partial示例1:
def func(a, b, c=0):
    return a - b + c

# 使用partial固定关键字参数c
new_func = partial(func, c=2)

# 在调用new_func时，只需要传入未预设的参数a和b
print(new_func(5, 3))  # 输出: 4

partial示例2:
# 假设有这样一个函数
def multiply(x, y):
    return x * y

# 使用partial来固定multiply函数的一个参数
double = partial(multiply, 2)

# 调用double时，只需要传入一个参数
print(double(4))  # 输出: 8
'''

'''
方法一：一次性读取所有内容，返回一个字符串数组，一行是数组中一个元素
'''
def get_lines(filename):
    with open(filename,'r') as f:
        return f.readlines()

'''
方法二：readline() 一次读取一行
'''
def get_line_by_line(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            print(line, end='')
            line = f.readline()


'''
方法三：用生成器逐行读取文件。
rb是以二进制读取的意思，对于读取非文本文件（如图像、视频、PDF文件等），使用二进制模式可
以确保文件内容不会在读取过程中被错误地修改或损坏。
文本文件，也可以使用二进制模式，但可能要手动处理字符编码和换行符。
'''
def generate_lines(filename):
    with open(filename,'rb') as f:
        for line in f:
            yield line

'''
方法四：一次性读取整个文件的内容到一个字符串中
'''
def get_file_content_str(filename):            
    with open(filename , 'r') as f:
        content = f.read()
        return content


'''
方法五：指定每次读取的字节数
'''
def read_file_in_chunks(filename, chunk_size=1024):
    """按给定大小读取文件内容"""
    with open(filename, 'rb') as file:  # 使用二进制模式打开文件
        for chunk in iter(partial(file.read, chunk_size), b''):
            yield chunk



if __name__ == '__main__':
    for e in generate_lines():
        print(e.strip()) # strip()去掉首尾空格或换行符
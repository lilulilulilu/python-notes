'''
some_str.split() 方法在 Python 中用于字符串分割，默认情况下，它会使用任何空白字符来分割字符串。这些空白字符包括空格、制表符（\t）、换行符（\n）、回车符（\r）和换页符（\f）。
'''
text = "Hello   world\nThis is an example.\tYes"
words = text.split()

print(words)  # 输出: ['Hello', 'world', 'This', 'is', 'an', 'example.', 'Yes']

# 反转字符串
s = "123456"
reversed_s = s[::-1]
print(reversed_s) # 输出: 654321


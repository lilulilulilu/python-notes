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

# https://www.w3schools.com/python/python_regex.asp
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

import re
re.findall("ai", "The rain in Spain") # ['ai', 'ai'],返回一个数组
re.search("ai", "The rain in Spain").span() # (5, 7)，返回一个元组，标志起始下标
re.sub(" ", "_", "The rain in Spain") # 'The_rain_in_Spain'，替换所有空格
re.split(" ", "The rain in Spain") # ['The', 'rain', 'in', 'Spain']，分割字符串

# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)







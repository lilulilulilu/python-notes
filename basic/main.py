from collections import deque, Counter, defaultdict
from queue import PriorityQueue
import heapq
import random
a = random.randint(0, 100) # 生成一个随机数,范围[0, 100]

q = deque()
q.append('a') # 添加元素到队列的右边
q.appendleft('d') # 添加元素到队列的左边
q.popleft() # 删除队列的左边第一个元素
q.pop() # 删除队列的右边第一个元素
q.rotate(2) # 将队列的元素向右旋转2步
q.rotate(-2) # 将队列的元素向左旋转2步
q.clear() # 清空队列
q.extend(['a', 'b', 'c']) # 添加多个元素到队列的右边

l = []
l.append('a')
l.pop() # 删除最后一个元素，in constant time
l.pop(3) # 删除第3个元素，in linear time
l.remove('a') # 删除列表中第一次出现的value，时间复杂度O(n)
l.extend(['d', 'e']) # 添加多个元素,时间复杂度O(k),原集合改变
i = l.index('d') # 返回元素的索引
l.insert(1, 'b') # 在指定位置插入元素
l.sort() # 排序，原list改变
l1 = sorted(l) # 排序，返回一个新的list

Counter('abcc') # Counter({'c': 2, 'a': 1, 'b': 1})
Counter(['a', 'b', 'c', 'c']) # Counter({'c': 2, 'a': 1, 'b': 1})
Counter({'a': 1, 'b': 2}) # Counter({'b': 2, 'a': 1})
Counter(a=1, b=2) # Counter({'b': 2, 'a': 1})
d1 = {}
d1['alice'] = 88
# 删除一个元素, in constant time
v = d1.pop('alice') # output: 88
k, v = d1.popitem() # output: ('bob', 77)
d = defaultdict(list) # 创建一个字典，值是一个列表
d[a].append('1') # 如果a不在字典中，会自动创建一个空列表,然后添加元素‘1’

# set是一个无序的集合，它不记录元素的插入顺序。这意味着当你遍历或打印一个set时，元素的顺序可能与插入顺序不同。
s = set()
s.add("a") #无返回值
s.remove('a') #删除指定元素,时间复杂度O(1)，无返回值
s.pop() #随机删除一个元素并将该元素返回
s.update(['a', 'b', 'c']) # 把列表中所有元素加入集合，原集合改变
s2 = s.union(['d', 'e']) # 把列表中所有元素加入集合，返回一个新集合
s3 = s2.copy()


# min heap
import heapq
min_heap = []
heapq.heappush(min_heap, (4, 'a', 'b')) # O(log n) 操作
heapq.heappush(min_heap, (2, 'a', 'c')) # O(log n) 操作
heapq.heappush(min_heap, (3, 'b', 'c')) # O(log n) 操作
print(heapq.heappop(min_heap)) # (2, 'a', 'c')



import re
re.findall("ai", "The rain in Spain") # ['ai', 'ai'],返回一个数组
re.search("ai", "The rain in Spain").span() # (5, 7)，返回一个元组，标志起始下标
re.sub(" ", "_", "The rain in Spain") # 'The_rain_in_Spain'，替换所有空格
re.split(" ", "The rain in Spain") # ['The', 'rain', 'in', 'Spain']，分割字符串
# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# 定义要分割的字符串
expression = "1-2+3-6"
# 使用正则表达式分割字符串
# \d+ 匹配一个或多个数字
# [+-] 匹配加号或减号
tokens = re.findall(r'\d+|[+-]', expression)
print(tokens) # ['1', '-', '2', '+', '3', '-', '6']
txt = "abcdcecfgh"

'''
index 和 find 都是 Python 中用于查找子字符串的方法，但它们处理查找不到子字符串的情况不同。
str.index(sub) 方法在字符串中查找子字符串 sub，如果找到，返回子字符串的第一个字符在字符串中的索引；如果找不到，会抛出一个 ValueError 异常。
str.find(sub) 方法也是在字符串中查找子字符串 sub，如果找到，返回子字符串的第一个字符在字符串中的索引；但如果找不到，不会抛出异常，而是返回 -1。
所以，当你确定子字符串一定存在于字符串中时，可以使用 index 方法；如果不确定，为了避免程序因为抛出异常而中断，应该使用 find 方法。'''
# str operations example:
print(txt.index("c")) # 2 , return the first occurence index of "c"，
print(txt.find("c")) # 2 找到返回第一个c的位置，找不到返回-1
print(txt.count("c")) # 3,计算c出现的次数
print(txt.replace("c", "C")) # abCdCefgh
print(txt.isdigit()) # False

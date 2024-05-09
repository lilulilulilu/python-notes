import random

l = []
l.append('a')
l[0] = 'b' # 时间复杂度O(1)
l.remove('b') # 时间复杂度O(n)，删除列表中第一次出现的value
l.extend(['d', 'e']) # 添加多个元素
l.pop() # 删除最后一个元素，in constant time
l.pop(0) # 删除第一个元素，in linear time
i = l.index('d') # 返回元素的索引 0， 如果元素不存在，抛出异常ValueError，时间复杂度O(n)
l.insert(1, 'b') # 在指定位置插入元素
l1 = sorted(l, key=lambda x: x, reverse=False) # 排序，返回一个新的list. []
l.sort(key=lambda x: x) # 排序，原list改变
map_it = map(lambda x: x * 2, [1, 2, 3]) # 返回一个迭代器
filter_it = filter(lambda x: x > 0, [-1, 0, 1, 2]) # 返回一个迭代器
reversed_it = reversed([2, 4, 6])
l2 = list(map_it) # [2, 4, 6]
l3 = list(reversed_it) # [6, 4, 2]

" ".join(['a', 'b', 'c']) # 'a b c'
#######创建list#########
# 1.创建一个普通的list，用random.shuffle将list打乱循序
l1 = [1,2,3,4,5]
# random.shuffle(l1) #l1被打乱顺序
map_it = map(lambda x: x * 2, [1, 2, 3]) # 返回一个迭代器
filter_it = filter(lambda x: x > 0, [-1, 0, 1, 2]) # 返回一个迭代器
l2 = list(map_it) # [2, 4, 6]
print(list(reversed(l2)))
s = ''.join(l2) # '21453' l1里的元素必须都是str类型，否则会报错


# 2.用map给生成新的list
def pow(num):
    return num ** 2
l2 = list(map(pow, l1)) # l2 = [1, 4, 9, 16, 25]
# 上面3行代码等价于下面的一行代码
l2 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
# 用reduce方法将list中的元素累加,reduce方法需要从functools模块导入
# 如果数组是字符串，则是拼接成一个完整的字符串，相当于"".join(list)
from functools import reduce
l = reduce(lambda x,y :x+y,['a', 'b', 'c']) # 'abc'
l = reduce(lambda x,y :x+y,[1,2,3,4]) # 10

# 3.用list comprehension生成新的list
l3 = [x**2 for x in l1] # l3 = [1, 4, 9, 16, 25

# 用dict comprehension生成新的dict
d1 = {x: x**2 for x in l1} # d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


###########list相关操作############
# 1.用sorted方法给list排序
l3 = sorted(l2)
print(l3)

# 2.在sorted方法中用key=lambda x: x[2]参数指定排序的key,
l4 = [
    ("Mike", "Thomson", 20, "M"),
    ("Robert", "Bustle", 32, "M"),
    ("Andria", "Bustle", 30, "F")
]
l5 = sorted(l4, key=lambda x: x[2], reverse=True) # 默认从小到大，加了reverse=True将从大到小排序
# [('Robert', 'Bustle', 32, 'M'), ('Andria', 'Bustle', 30, 'F'), ('Mike', 'Thomson', 20, 'M')]

# 3.计算两个list中的相同元素和不同元素
A = [1, 2, 3]
B = [2, 3, 4]
# A,B 中相同元素： 
print(set(A)&set(B)) # output: {2, 3}
# A,B 中不同元素:  
print(set(A)^set(B)) # output: {1, 4}




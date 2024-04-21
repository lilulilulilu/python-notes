import random

#######创建list#########
# 1.创建一个普通的list，用random.shuffle将list打乱循序
l1 = [1,2,3,4,5]
random.shuffle(l1) #l1被打乱顺序

# 2.用map给生成新的list
def pow(num):
    return num ** 2

l2 = list(map(pow, l1)) # l2 = [1, 4, 9, 16, 25]

# 上面3行代码等价于下面的一行代码
l2 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数


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




import random
l1 = [1,2,3,4,5]
random.shuffle(l1) #l1被打乱顺序
print(l1)

def pow(num):
    return num ** 2

l2 = list(map(pow, l1))
print(l2)

l3 = sorted(l2)
print(l3)

l4 = [
    ("Mike", "Thomson", 20, "M"),
    ("Robert", "Bustle", 32, "M"),
    ("Andria", "Bustle", 30, "F")
]

l5 = sorted(l4, key=lambda x:x[2], reverse=True)
print(l5)


A = [1, 2, 3]
B = [2, 3, 4]
# A,B 中相同元素： 
print(set(A)&set(B)) # output: {2, 3}

# A,B 中不同元素:  
print(set(A)^set(B)) # output: {1, 4}

# 帮我写一个快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


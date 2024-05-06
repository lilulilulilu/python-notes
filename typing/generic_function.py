
from typing import TypeVar, List

# 创建一个类型变量'T', 即泛型T
T = TypeVar('T')

# 使用TypeVar 'T' 创建泛型函数
def first_element(sequence: List[T]) -> T:
    return sequence[0]

# generic function
def f(e: T) -> T:
    return e
print("f(5):", f(5))

def first_item(l: list):
    return l[0]


if __name__ == "__main__":
    l1: List[int] = [1,2,3]
    l2: List[str] = ['a', 'b', 'c']
    
    print(first_element(l1))
    print(first_element(l2))
    print(first_item(l1))
    print(first_item(l2))

'''
(base) qqli@qqdeMacBook-Pro typing % python main.py
1
a
1
a
'''
    
'''
自定义一个iterable类Node，可以用forloop遍历
如果__iter__函数返回的比是一个generator，就必须实现__next__函数，才可以用forloop遍历
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        v_iter = self.val  # v_iter一直是第一个节点的值
        self.current = self  # 这一行必不可少
        return self

    def __next__(self):
        v_next = self.val  # v_next一直是第一个节点的值
        if self.current is None:
            raise StopIteration
        else:
            current = self.current  # 保持当前节点的引用
            self.current = self.current.next  # 移动到下一个节点
            return current

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n1.next = n2
n2.next = n3
n3.next = n4
   
# 这个循环只调用一次n1.__iter__()方法，然后每次循环的时候执行 n = n1.__next__()，直到抛出StopIteration异常
# 所以在__next__方法中要保存上一次访问的节点，以便能找到下一个节点，否则会一直返回第一个节点n1
for n in n1: # n1的类型是Node，所以会调用n1.__iter__()方法，返回一个迭代器，迭代器有__next__()方法，所以可以用for循环
    print(n.val) # 1 2 3 4
    
    
# 使用 while 循环迭代
# iterator = iter(n1)  # 获取迭代器
# while True:
#     try:
#         n = next(iterator)  # 获取下一个元素
#         print(n.val)
#     except StopIteration:  # 当没有更多元素时，抛出 StopIteration 异常
#         break  # 终止循环

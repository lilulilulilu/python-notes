'''
1.自定义一个iterable类Node，可以用forloop遍历。
实现方式一：如果__iter__函数返回的是一个generator，就不需要实现__next__函数，也可以用forloop遍历
实现方式二（见node_iterable_iter_next）：如果__iter__函数返回的不是一个generator，就必须实现__next__函数，才可以用forloop遍历
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    # 此方法不实现的话，forloop会报错: TypeError: 'Node' object is not iterable      
    def __iter__(self):
        node = self
        while node is not None:
            yield node   # 在这个例子里，iter必须用yield返回结果，不能用return，否则没法forloop
            node = node.next
    
    # 此方法不实现的话，next(Node)会报错: TypeError: 'Node' object is not an iterator       
    # def __next__(self):
    #     if self.next is None:
    #         raise StopIteration
    #     node, self = self, self.next
    #     return node
    
if __name__ == '__main__':
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    # first = next(n1) # 这行需要放出上面的__next__方法，才能执行成功
    # print("first:", first.val)
    for n in n1:
        print(n.val)
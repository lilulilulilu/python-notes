'''
生成器是一种特殊的迭代器
'''

# # 生成器函数
# def gen(nums):
#     while nums > 0:
#         yield nums
#         nums -= 1
#     return

# #调用生成器函数会生成一个生成器对象
# g = gen(5)

# #对生成器对象使用next函数才开始真正执行函数本体
# first = next(g)

# for i in g:
#     print(i)


# iterable     
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
    
if __name__ == '__main__':   
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node1.next = node2
    node2.next = node3

    for node in node1:
        print(node.val)
        
        
    it = iter(node1)  
    print(next(it).val) 
    print(next(it).val) 
    print(next(it).val) 

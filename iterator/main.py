'''
iterable（数据的保存者，可以产生一个iterator）
可迭代对象，例如list,str，tuple,dict, file objects, 带__iter__()方法或者__getitem__()方法的类；
可用for loop一个一个的访问。

iterator（）
一个表示数据流的对象，可以用next()不断的从这个对象里取出数据
必须有__next__()方法，

'''

# l1 = [1,2,3]

# for i in l1:
#     print(i)
    

class NodeIterator:
    def __init__(self,node):
        self.curr_node = node
    
    def __next__(self):
        if  self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node
    
    def __iter__(self):
        return self
    
 
# iterable     
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __iter__(self):
        return NodeIterator(self)
    
if __name__ == '__main__':     
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node1.next = node2
    node2.next = node3

    for node in node1:
        print(node.val)
        
    it = iter(node1)
    first = next(it)
    '''
    NodeIterator必须实现:
        def __iter__(self):
            return self
    不然下面的循环会报错
    '''
    for node in it:
        print(node.val)
class Node():
    def __init__(self,key, val=0, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

class CapacityList():
    def  __init__(self):
        self.head = None
        self.tail = None

    # add a new node to tail
    def add(self, node):
        node.pre = self.tail
        node.next = None
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    # 把node移到队尾
    def update(self, node): 
        if node == self.tail:
            return
        node_pre = node.pre
        node_next = node.next
        if node == self.head:
            if self.head.next:
                self.head = self.head.next

        if self.tail:
            self.tail.next = node
            node.next = None
            node.pre = self.tail
            self.tail = node
            if node_pre:
                node_pre.next = node_next
            if node_next:
                node_next.pre = node_pre

    def pop_lru(self):
        h = self.head
        self.head = h.next
        return h


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.q = CapacityList()

    def get(self, key: int) -> int:         
        if key in self.d:
            node = self.d[key]
            value = node.val 
            self.q.update(node)
            return value
        return -1       

    def put(self, key: int, value: int) -> None:
        # 新增key，节点放到q末尾
        if key not in self.d:
            node = Node(key,value)
            length = len(self.d)
            if length < self.capacity:
                self.d[key] = node # 如果还有空位，则直接加入字典
                self.q.add(node) # 同时队列中也加入一个元素
            else: # 长度满了，弹出lru
                lru_node = self.q.pop_lru() #队列中的元素和字典中元素一致
                self.d.pop(lru_node.key) # 字典中弹出key的元素
                self.d[key] = node
                self.q.add(node) # node放队尾，优先级变得更不容易被删掉
        else: # 如果key已经在字典中，更新node的值，并改变队列中的优先级
            node = self.d[key]
            node.val = value
            self.q.update(node)

# lRUCache = LRUCache(1) 
# lRUCache.put(10, 13)  # cache is {1=1}
# lRUCache.put(3, 17)  # cache is {1=1, 2=2}
# lRUCache.put(6, 11)  # cache is {1=1, 2=2}
# lRUCache.put(10, 5)  
# lRUCache.put(9, 10)  # cache is {1=1, 2=2}
# print(lRUCache.get(13) )  -1
# lRUCache.put(2, 19)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2) )   
# print(lRUCache.get(3) )    # returns -1 (not found)
# lRUCache.put(5, 25)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(8)  ) 
# lRUCache.put(9, 12)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.put(5, 5)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}

lRUCache = LRUCache(1) 
lRUCache.put(2, 1)
print(lRUCache.get(2) ) 
lRUCache.put(3, 2)
print(lRUCache.get(2) ) 
print(lRUCache.get(3) ) 




            
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
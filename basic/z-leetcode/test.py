from collections import deque
# 1.array
arr = []

# 2. linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.nxt = None
        self.pre = None
head = Node(0) # root, tail, nxt, pre

# 3.stack
stack=[]


# 4.queue
q = deque()
q.append('a')

# 5.set
ss = set()

# 6.map
d = {}

# 7.heap
import heapq
min_heap = []
heapq.heappush(min_heap, (4, 'a', 'b')) # O(log n) 操作
heapq.heappush(min_heap, (2, 'a', 'c')) # O(log n) 操作
heapq.heappush(min_heap, (3, 'b', 'c')) # O(log n) 操作
print(heapq.heappop(min_heap)) # (2, 'a', 'c')

# 8. graph
from collections import defaultdict
graph = defaultdict(list)
graph['a'] = ['b', 'c', 'd']
graph['b'] = ['e']  
graph['c'] = ['e']
graph['d'] = ['f']
graph['e'] = ['g']
graph['f'] = ['g']


# 9. tree
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        



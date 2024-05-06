import heapq

# 这个实现只能是数字的最大堆
class MaxHeap():
    def __init__(self) -> None:
        self.heap = []
        self.size = 0
    
    def push(self, val):
        heapq.heappush(self.heap, -val) # 用负数实现最大堆,所以这个堆只能放数字
        
    def pop(self):
        return -heapq.heappop(self.heap)
    
    def __len__(self):
        return len(self.heap)
    
    
if __name__ == "__main__":
    maxheap = MaxHeap()
    maxheap.push(3)
    maxheap.push(2)
    maxheap.push(1)
    maxheap.push(5)
    
    while maxheap:
        print(maxheap.pop()) # 5, 3, 2, 1
        

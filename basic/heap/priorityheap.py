import heapq

heap = []
heapq.heappush(heap, (3,'c'))
heapq.heappush(heap, (4, 'd'))
heapq.heappush(heap, (5, 'ee'))
heapq.heappush(heap, (2, 'bb'))
while heap:
    print(heapq.heappop(heap)) # (2, 'bb'), (3, 'c'), (4, 'd'), (5, 'ee')



x = [(3, 1), (5,3), (4,5), (5, 6)]    
heapq.heapify(x) # 根据第一个元素排序
print("x", x) # [(3, 1), (5, 3), (4, 5), (5, 6)], 堆化后的x不一定有序，但是肯定是堆
while x:
    print(heapq.heappop(x))  # (3, 1), (4, 5), (5, 3), (5, 6)
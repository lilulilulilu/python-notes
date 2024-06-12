import bisect
class Solution:
  def __init__(self):
    self.arr = []  
 
  def connect(self, part1, part2):
    return [min(part1[0], part2[0]), max(part1[1], part2[1])]
    
  def union(self, start, end) -> None:
    if start > end:
        raise ValueError("start should be less than end. start: %d, end: %d" % (start, end))  
    n = len(self.arr)
    if n == 0:
      self.arr.append([start, end]) 
      return
    #头部
    if start > self.arr[n-1][1]: #追加在尾部
      self.arr.append([start, end])
      return  
    elif start >= self.arr[n-1][0]: # 仅仅和最后一个区间相连
      self.arr[n-1] = self.connect(self.arr[n-1], [start, end])
      return      
    #尾部
    if end < self.arr[0][0]: #追加的头部
      self.arr.insert(0, [start, end])
      return
    elif end <= self.arr[0][1]: #仅仅和第一个区间相连
      self.arr[0] = self.connect(self.arr[0], [start, end])
      return  
    #新加入的节点连接了头和尾
    if start <= self.arr[0][1] and end >= self.arr[n-1][0]:
      part = self.connect(self.arr[0],self.arr[n-1])
      self.arr = self.connect(part, [start, end])
      return
    #新加入的节点在中间             
    a = bisect.bisect_right(self.arr, start, key=lambda x: x[0])-1 #在起点集合中，找到最大的小于等于start的位置， 编号为 0 的列要有序，否则比较没有意义
    b = bisect.bisect_right(self.arr, end, key=lambda x: x[1])   #在终点集合中，找到最小的大于end的位置， 编号为 1 的列要有序，否则比较没有意义
    for i in range(a+1, b):
      self.arr.pop(i)   
    if start > self.arr[a][1]: # 和a不相连
      if a + 1 < len(self.arr):
        if end < self.arr[a+1][0]: # 和b不相连
          self.arr.insert(a+1, [start, end])
        else: # 和b相连
          self.arr[a+1] = self.connect(self.arr[a+1], [start, end])
    else: # 和a相连
      self.arr[a] = self.connect(self.arr[a], [start, end])
      if a + 1 < n: #如果同时还和b相连
        if end >= self.arr[a+1][0]:
          self.arr[a] = self.connect(self.arr[a+1], self.arr[a])
          self.arr.pop(a+1)
  
  def find(self, num) -> bool:
    n = len(self.arr)
    i = 0
    j = n-1
    while i <= j:
      mid = (i+j) // 2
      if self.arr[mid][1] < num :
        i = mid+1
      elif self.arr[mid][0] > num:
        j = mid-1
      elif self.arr[mid][0] <= num <= self.arr[mid][1]:
        return True
    return False


s = Solution()
s.union(2,5)
s.union(9,13)
print(s.arr)
print('--------------------')
print(f'[6,8] -> {s.arr}')
s.union(6,8)
print(s.arr)
print('--------------------')
print(f'[7,7] -> {s.arr}')
s.union(7,7)
print(s.arr)

print('--------------------')
print(f'[8.5,8.5] -> {s.arr}')
s.union(8.5,8.5)
print(s.arr)

print('--------------------')
print(f'[9,9] -> {s.arr}')
s.union(9,9)
print(s.arr)

print('--------------------')
print(f'[9,10] -> {s.arr}')
s.union(9,10)
print(s.arr)
    
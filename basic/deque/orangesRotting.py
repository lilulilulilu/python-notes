from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 遍历一遍grid，收集有传染性的的水果放入一个队列q1，好水果放入集合s
        # 当集合s还存在好水果时：
        # 1.对q1中的元素出队：
        #（1）对出队的元素做如下处理：检查该元素的上下左右的水果，好水果从集合s中删除，如果该好水果还有传染性，放到下一轮的队列q2；
        # 2.时间增加1秒
        # 3.q1和q2互换, 直到所有水果已经变坏
        row = len(grid)
        column = len(grid[0])
        times = 0

        # 上下左右有一个好的，那就是有传染性
        def isContagious(orange: tuple[int, int]) -> bool:
            i, j = orange
            if ((i-1 >=0 and grid[i-1][j] == 1) or 
                (i+1 < row and grid[i+1][j] == 1) or
                (j-1 >= 0 and grid[i][j-1] == 1) or 
                (j+1 < column and grid[i][j+1] == 1)):
                return True
            return False

        q = deque()
        s = set()
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2 and isContagious((i,j)):
                    q.append((i,j))
                elif grid[i][j] == 1:
                    s.add((i,j))
        q2 = deque()

        def helper(orange: tuple[int,int]) -> None:
            if orange in s:
                s.remove(orange)
                if isContagious(orange):
                    q2.append(orange)
                        
        while s:  #当集合s还有元素时               
            while q:
                i, j = q.popleft()
                if i-1 >=0 and grid[i-1][j] == 1:
                    helper((i-1,j))
                if i+1 < row and grid[i+1][j] == 1:
                    helper((i+1,j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    helper((i,j-1))
                if j+1 < column and grid[i][j+1] == 1:
                    helper((i,j+1))

            times = times + 1
            q, q2 = q2, q
            if len(q) == 0 and len(q2) == 0 and len(s) != 0:
            # if not q and not q2 and s:   当队列q和q2都为空，且s还有元素的时候
                return -1

        return times
             
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid)) # 4

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(grid)) # 4


grid = [[0,2]]
print(Solution().orangesRotting(grid)) # 0








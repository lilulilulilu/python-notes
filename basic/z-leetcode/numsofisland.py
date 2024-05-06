'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    row = len(grid)
    if row == 0 :
        return 0
    column = len(grid[0])  

    # 判断点(i,j)的上下左右是不是为1，如果是则加入队列集合中queue_set，用set保证已加入的不会重复添加
    def helper(grid, i, j, queue_set, row, column):
          # left, up, right, down
        if j-1 >= 0 and grid[i][j-1] == '1': 
            queue_set.add((i, j-1)) 
        if i-1 >= 0 and grid[i-1][j] == '1':
            queue_set.add((i-1, j))
        if j+1 < column and grid[i][j+1] == '1': 
            queue_set.add((i, j+1))
        if i+1 < row and grid[i+1][j] == '1': 
            queue_set.add(( i+1, j))   

    count = 0
    queue_set = set()
    # 从左到右，从上到下的方向，遍历二维表格的每个元素, 借助集合，以深度优先的方式，将岛屿一个个消除：
    # 每碰到一个新的岛屿，count加1，然后将该岛屿从地图上消除
    for i in range(row):
        for j in range(column):
            if grid[i][j] == '1':
                queue_set.add(( i, j))
                count = count + 1
                # eliminate grid[i][j] itself and all the connected number
                while len(queue_set) != 0:
                    temp_i, temp_j = queue_set.pop()
                    grid[temp_i][temp_j] = 0
                    helper(grid, temp_i, temp_j, queue_set, row, column)

    return count


                    


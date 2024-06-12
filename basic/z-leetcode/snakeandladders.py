from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if n * n <= 6:
            return 1

        d = {} # key is label, value is the position (i,j)
        k = 1
        i = n-1
        while i >= 0:
            for j in range(n):
                d[k] = (i, j)
                k += 1
            i = i - 1
            if i >= 0:
                for j in range(n-1, -1, -1):
                    d[k] = (i, j)
                    k += 1
            i = i - 1
        
        visited = [0] * (n*n+1)

        def min_step(board, start) -> int:
            if start+6 >= n*n :
                return 1
            q = deque()
            for label in range(start+1, start+7, 1):
                if visited[label] != 1:
                    i, j = d[label]
                    if board[i][j] != -1:
                        q.append(board[i][j])
                    else:
                        if label == start+6:
                            q.append(label)
                    visited[label] = 1
                    
            if len(q) == 0:
                return None 
            
            candidates = [min_step(board, label) for label in q] 
            candidates = [c for c in candidates if c != None]
            if candidates:
                return 1 + min(candidates)
            else:
                return None           

        result = min_step(board, 1)
        if result == None:
            return -1
        else:
            return result


board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(board)) # 4       


        


from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        startDict = defaultdict(list) # key: character, value:[(i,j)], position list
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                startDict[board[i][j]].append((i,j))

        def getAjacentsPosition(board, position, c) -> list[tuple]:
            result = []
            i, j = position
            for x, y in [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]:
                if x >= 0 and x < m and y >= 0 and y < n:
                    if board[x][y] == c:
                        result.append((x,y))
            return result

        def dfs(board, position, word, visited) -> bool: #从position开始查找word，能找到则返回True
            i,j = position
            if len(word) == 1 and board[i][j] == word[0] and position not in visited:
                return True  
            visited.add(position)
            ajacentsPosition = getAjacentsPosition(board, position, word[1]) #find the position whose value is word[1]
            for p in ajacentsPosition:
                if p not in visited:
                    exist = dfs(board, p, word[1:], visited)
                    if exist:
                        return True
            if position in visited:
                visited.remove(position)
            return False
            

        result = set()
        words = list(set(words))
        for word in words:
            starts = startDict[word[0]]
            for start in starts:
                visited = set()
                exist = dfs(board, start, word, visited)
                if exist:
                    result.add(word)           
        
        return list(result)

print(Solution().findWords([["a","a"]], ["aaa"])) # []
print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) # ["oath","eat"]


def dfs(board, position, trie, visited):
    pass
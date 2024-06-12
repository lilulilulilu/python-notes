from collections import defaultdict
from typing import List

class Trie:
    def __init__(self):
        self.d = {}

    def find(self, word) -> bool:
        p = self
        for c in word:
            if c in p.d:
                p = p.d[c]
            else:
                return False
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        def getAdjacents(board, position, visited) -> list[tuple]:
            result = []
            i, j = position
            for x, y in [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]:
                if x >= 0 and x < m and y >= 0 and y < n:
                    if (x,y) not in visited:
                        result.append((x,y))
            return result
                
        def dfs(board, position, trie, visited):
            i, j = position
            c = board[i][j]
            p = trie
            if c in p.d:
                p = p.d[c]
            else:
                node = Trie()
                p.d[c] = node
                p = node
            visited.add(position)
            adjacents = getAdjacents(board, position, visited)
            for start in adjacents:
                visited2 = visited.copy()
                dfs(board, start, p, visited2)
            return trie
        
        def createTrie(board) -> Trie:
            trie = Trie()
            for i in range(m):
                for j in range(n):
                    visited = set()
                    dfs(board, (i,j), trie, visited)
            return trie

        trie = createTrie(board)
        result = set()
        for word in words:
            if trie.find(word):
                result.add(word)          
        return list(result)
    
board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().findWords(board, words)) # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
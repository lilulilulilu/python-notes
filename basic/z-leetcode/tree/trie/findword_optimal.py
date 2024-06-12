from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        # 构建字典树（前缀树）以存储所有单词
        trie = {}   
        for w in words:
            p = trie
            for c in w + "#":  # "#" 作为单词结束标志
                if c not in p:
                    p[c] = {}
                p = p[c]
        
        res = []  # 用于存储可以在 board 中找到的单词

        # 从位置 (i, j) 开始递归搜索，将所有可能在 board 中找到的单词添加到 res 中
        # dic 是 trie 中当前字符的子树，prefix 是当前构建的前缀
        def dfs(visited, i, j, dic, prefix):
            # 如果当前子树中有终结符，说明 prefix 是一个完整单词，加入 res
            if '#' in dic:
                res.append(prefix)
                del dic['#']  # 删除终结符，避免重复添加相同单词
            visited.add((i, j))  # 标记当前位置为已访问
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    c = board[x][y]  # 邻居字符
                    if c in dic:  # 邻居字符在子树中，继续深度优先搜索
                        dfs(visited, x, y, dic[c], prefix + c)
                        if len(dic[c]) == 0:
                            del dic[c]  # 清理已处理完的子树            
            visited.remove((i, j))# 回溯，移除当前位置的访问标记

        # 遍历 board，找到所有以 i,j 为起点的可能单词
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in trie:  # 如果字符在字典树的根节点中
                    dfs(set(), i, j, trie[c], prefix=c)
                    if len(trie[c]) == 0:
                        del trie[c]  # 清理已处理完的子树        
        return res

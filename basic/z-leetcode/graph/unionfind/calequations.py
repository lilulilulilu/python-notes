from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        for equation in equations:
            v1, v2 = equation
            variables.add(v1) 
            variables.add(v2) 

        n = len(variables)
        index = {}
        i = 0
        for e in variables:
            index[e] = i
            i = i + 1
            
        uf = UnionFind(n)
        for equation, value in zip(equations, values):
            v1, v2 = equation
            uf.connected(index[v1], index[v2], value)

        results = []
        for query in queries:
            v1, v2 = query
            result = -1
            if v1 not in variables or v2 not in variables: # 如果有变量不存在则返回-1
                result = -1
            elif uf.isConnected(index[v1], index[v2]) is not True:
                result = -1
            else:
                result = (1/uf.weight[index[v1]]) * uf.weight[index[v2]]

            results.append(result)
        return results
                                                                                                                          

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # 存放根节点编号
        self.weight = [1 for _ in range(n)] # 到根节点的值
        self.n = n
        
    def connected(self, i, j, value):
        parent_j = self.parent[j]
        weight_j = self.weight[j] # root/j的值
        for k in range(self.n):
            if self.parent[k] == parent_j:
                self.parent[k] = self.parent[i]
                self.weight[k] = self.weight[k] * value / weight_j

    def isConnected(self, i, j) -> bool:
        return self.parent[i] == self.parent[j]

equations = [["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]] 
values = [2.0,3.0,4.0,5.0,6.0,7.0,8.0]
queries = [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]]
print(Solution().calcEquation(equations, values, queries))
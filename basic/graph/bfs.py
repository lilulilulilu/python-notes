from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()
    result = []
    q = deque([start])
    while q:
        node = q.popleft() #出队一个元素，没被访问过则加入到结果中，然后将其邻居加入到队列中
        if node not in visited:
            result.append(node)
            visited.add(node) # 将当前访问了的所有邻居节点加入队列中
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
    return result


print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
            
from collections import deque

def bfs(graph, start):
    # 创建一个队列并将起始节点加入队列
    queue = deque([start])
    # 创建一个集合用于记录访问过的节点
    visited = set([start])
    
    while queue:
        # 从队列中弹出一个节点
        current = queue.popleft()
        
        # 访问该节点（这里我们可以根据需求处理该节点）
        print(current)
        
        # 遍历当前节点的所有邻居节点
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 示例图的表示（邻接表）
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 从节点 'A' 开始执行BFS
bfs(graph, 'A')

'''
广度优先搜索（Breadth-First Search, BFS）是一种用于遍历或搜索图或树的算法。它从根节点开始，首先访问所有相邻节点，然后再逐层向外扩展，直到访问完所有节点或找到目标节点。

BFS的思想
1.队列（Queue）数据结构：
    BFS使用队列来实现。队列是一种先进先出（FIFO）的数据结构。
2.访问和标记节点：
    从起始节点开始，将其标记为已访问并放入队列中。
    从队列中取出一个节点，访问它的所有未访问过的邻居节点，并将这些邻居节点标记为已访问，然后依次入队。
    重复上述过程，直到队列为空或找到目标节点。
BFS(graph, start_node):
    1. 创建一个空队列 queue
    2. 将 start_node 放入队列 queue
    3. 创建一个集合 visited，用于存储已访问的节点

    4. while queue 不为空:
        5. 从队列 queue 中取出一个节点 current
        6. if current 是目标节点:
            7. 返回 current

        8. for each 邻居节点 neighbor of current:
            9. if neighbor 不在 visited 中:
                10. 将 neighbor 标记为已访问
                11. 将 neighbor 放入队列 queue

    12. 如果队列为空且没有找到目标节点，返回 None
'''

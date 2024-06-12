

from pprint import pprint


class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    def display(self):
        pprint(self.graph)

# 创建加权图
wg = WeightedGraph()

# 添加边
wg.add_edge('A', 'B', 5)
wg.add_edge('A', 'C', 10)
wg.add_edge('B', 'C', 2)



# 显示图
wg.display()
# 带权图
weighted_graph ={
    'A': {'B': 5, 'C': 10}, 
    'B': {'A': 5, 'C': 2}, 
    'C': {'A': 10, 'B': 2}
}

double_drected_weigted_graph = {
    'A': {'B': 5, 'C': 10}, 
    'B': {'A': 5, 'C': 2}, 
    'C': {'A': 10, 'B': 2}
}

# 无权图
graph = { 
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}




from collections import defaultdict
graph = defaultdict(list) 
graph['a'] = ['b', 'c', 'd']
graph['b'] = ['e']
graph['c'] = ['e']
graph['d'] = ['f']
graph['e'] = ['g']
graph['f'] = ['g']

ind = 'indegree'
out = 'outdgree'

def topology(graph: dict) -> list:
    
    g = defaultdict(dict)
    
    for k, v in graph.items():
        for node in v:
            if 'indegree' not in g[node]:
                g[node]['indegree'] = set()
            g[node]['indegree'].add(k)
            if 'outdegree' not in g[k]:
                g[k]['outdegree'] = set()
            g[k]['outdegree'].add(node)
    
    zero_indegree_nodes = [] # 零度表
    for k, v in g.items():
        if 'indegree' not in g[k] or len(g[k]['indegree']) == 0:
            zero_indegree_nodes.append(k)
            
    visited = []     
    while zero_indegree_nodes:
        node = zero_indegree_nodes.pop()
        visited.append(node)
        
        if 'outdegree' in g[node]:
            for n in g[node]['outdegree']:
                g[n]['indegree'].remove(node)
                if len(g[n]['indegree']) == 0:
                    zero_indegree_nodes.append(n)
                
    if len(visited) == len(g):
        return visited
    else:
        return -1
        

    
print(topology(graph))
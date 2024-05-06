'''
 Two Ways to Represent GRAPHS
 1.Adjacency List
 2.Adjacency Matrix
'''

from collections import defaultdict
weighted_graph = defaultdict(dict)
weighted_graph['1']['2'] = 1 # 1->2, weight 1
weighted_graph['2']['1'] = 1 # 2->1, weight 1
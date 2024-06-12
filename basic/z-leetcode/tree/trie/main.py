from collections import defaultdict
from functools import reduce
words = ["word", "war", "was"]
Trie = lambda: defaultdict(Trie)
trie = Trie()
for w in words: reduce(dict.__getitem__,w+'#',trie)        
print(trie)      


words = ["word", "war", "was"]
words = [w+"#" for w in words]
trie = {}
for w in words:
    p = trie
    for c in w:
        if c not in p:
            d = {}
            p[c] = d
            p = d
        else:
            p = p[c]
print(trie) # {'w': {'o': {'r': {'d': {'#': {}}}}, 'a': {'r': {'#': {}}, 's': {'#': {}}}}
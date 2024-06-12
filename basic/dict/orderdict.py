from collections import OrderedDict

# d = OrderedDict()
d = {}

d['a'] = 1
d['d'] = 2
d['c'] = 3
d['e'] = 3
d[7] = 6
d[0] = 0
for k, v in d.items():
    print(k, v)
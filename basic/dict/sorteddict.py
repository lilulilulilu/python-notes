from sortedcontainers import SortedDict

# 创建一个 SortedDict 实例
sorted_dict = SortedDict()

# 插入一些键值对
sorted_dict['banana'] = 3
sorted_dict['apple'] = 4
sorted_dict['pear'] = 1
sorted_dict['orange'] = 2

# 打印当前的排序字典
print("SortedDict: ", sorted_dict) # SortedDict:  SortedDict({'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1})

# 使用 bisect_left 和 bisect_right 方法
key_to_insert = 'grape'

left_index = sorted_dict.bisect_left(key_to_insert)
right_index = sorted_dict.bisect_right(key_to_insert)

print(f"bisect_left('{key_to_insert}') = {left_index}")
print(f"bisect_right('{key_to_insert}') = {right_index}")

# 插入键，并确保顺序
sorted_dict.update({key_to_insert: 5})
print("After inserting 'grape': ", sorted_dict)

# 使用 keys, values, items 方法
print("Keys: ", list(sorted_dict.keys()))
print("Values: ", list(sorted_dict.values()))
print("Items: ", list(sorted_dict.items()))

# 使用 popitem 和 peekitem 方法
print("Peek first item: ", sorted_dict.peekitem(0))
print("Peek last item: ", sorted_dict.peekitem())

print("Pop first item: ", sorted_dict.popitem(0))
print("After popping first item: ", sorted_dict)

print("Pop last item: ", sorted_dict.popitem())
print("After popping last item: ", sorted_dict)

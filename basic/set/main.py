# set是一个无序的集合，它不记录元素的插入顺序。这意味着当你遍历或打印一个set时，元素的顺序可能与插入顺序不同。
s = set()
s.add("a") #无返回值
s.remove('a') #删除指定元素,时间复杂度O(1)，无返回值
s.pop() #随机删除一个元素并将该元素返回
s.update(['a', 'b', 'c']) # 把列表中所有元素加入集合，原集合改变
s.update({2,3})

s2 = s.union(['d', 'e']) # 把列表中所有元素加入集合，返回一个新集合
s3 = s2.copy()

l = []
l.append('a')
l.remove('a') # 删除列表中第一次出现的value，时间复杂度O(n)
l.extend(['d', 'e']) # 添加多个元素,时间复杂度O(k),原集合改变
i = l.index('d') # 返回元素的索引
l.insert(1, 'b') # 在指定位置插入元素
l.pop() # 删除最后一个元素，in constant time
l.sort() # 排序，原list改变
l1 = sorted(l) # 排序，返回一个新的list




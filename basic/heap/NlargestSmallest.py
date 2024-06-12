import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]，时间复杂度为O(nlogk)，k为要找的最大的k个数，n为数组的长度
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

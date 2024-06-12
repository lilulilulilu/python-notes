from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(start, nums): # 递归过程中改变nums数组的值，把符合要求的nums数组copy一份放入结果集
            if len(nums) == k:
                res.append(nums.copy())
                return
            for i in range(start, n+1): #遍历[1,n]的所有元素
                nums.append(i) # 扩大部分解的范围
                bt(i+1, nums) #递归访问子树中的剩余解
                nums.pop() # 弹出的是i+1
        
        bt(1, [])

        return res
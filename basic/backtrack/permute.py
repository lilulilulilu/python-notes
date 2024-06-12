from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        返回nums的全排列，时间复杂度O(n!)
        '''
        res = []
        n = len(nums)

        def bt(nums, pre: List[int], visited: set) -> None:
            if len(pre) == n:
                res.append(pre)
                return
            for i in range(n):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    bt(nums, pre + [nums[i]], visited)
                    visited.remove(nums[i])
        pre = []
        bt(nums, pre, set())
        return res
    
print(Solution().permute(['a', 'b', 'c'])) 
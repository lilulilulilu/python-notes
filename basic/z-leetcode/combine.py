from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_k(nums: set, k: int) -> List[List[int]]:
            n = len(nums)
            if n == 1 and k == 1:
                return [list(nums)]
            if k == 1:
                return [[i] for i in nums]
            
                
            firsts = [i for i in nums]
            result = []
            for f in firsts:
                nums2 = nums.copy()
                nums2.remove(f)
                subcombines = combine_k(nums2, k-1)
                for subcombine in subcombines:
                    result.append([f]+subcombine)
            return result

        nums = {i+1 for i in range(n)}
        return combine_k(nums, k)
print(Solution().combine(4, 2))
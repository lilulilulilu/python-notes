import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def findK(nums, start, end, k) -> int:
            ri = random.randint(start, end+1)
            nums[end], nums[ri] = nums[ri], nums[end]
            pivot = nums[end]
            i = start
            j = end
            while i < j:
                while i < j and nums[i] > pivot:
                    i += 1
                nums[j] = nums[i]
                while i < j and nums[j] <= pivot:
                    j -= 1
                nums[i] = nums[j]
            nums[i] = pivot 

            if i-start == k-1:
                return nums[i]   
            if i-start > k-1:
                return findK(nums, start, i-1, k)
            if i-start < k-1:
                return findK(nums, i+1, end, k-i-1+start)

        return findK(nums, 0, len(nums)-1, k)  
    
print(Solution().findKthLargest([5,2,4,1,3,6,0], 4)) # 4
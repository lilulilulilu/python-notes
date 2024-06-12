from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def searchMin(nums, s, e) -> int:
            if s > e:
                return None
            if s == e:
                return nums[s]
            mid = (s + e) // 2
            if nums[mid] == nums[s]:
                return min(nums[s], nums[e])
            if nums[mid] > nums[s]: #left is sorted
                min_num = searchMin(nums, mid+1, e)
                if min_num is not None:
                    return min(nums[s], min_num)
                else:
                    return nums[s]
            if nums[mid] < nums[s]: #right is sorted
                min_num =  searchMin(nums, s, mid-1)
                if min_num is not None: 
                    return min(nums[mid], min_num)
                else:
                    return nums[mid]
        
        return searchMin(nums, 0, len(nums)-1)
    
print(Solution().findMin([4,5,6,7,0,1,2]))
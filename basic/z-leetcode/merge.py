from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        k = m + n - 1
        i = m - 1
        j = n - 1

        while k >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1

        if k >= 0 and i < 0:
            while j >= 0:
                nums1[k] = nums2[j]
                j = j - 1
                k = k - 1
                              
            
if __name__ == '__main__':
    solution = Solution()
    nums1=[1,2,3,0,0,0]
    nums2 = [2,5,6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)
    
    
    
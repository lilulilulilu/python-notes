from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # maxStreakLen = 0
        # 遍历每个元素：
        # 技巧点：如果n-1存在，则代表n不是起始数，跳过，我们只关心起始数
        # 否则如果n-1不存在，则判断n+1,n+2,..., n+k是否nums集合中，直到找不到连续的数了，maxStreakLen=max(maxStreakLen, k)
        maxStreakLen = 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                k = 1
                while n + k in nums:
                    k += 1
                maxStreakLen=max(maxStreakLen, k)
        return maxStreakLen

if __name__ == '__main__':
    solution = Solution()
    nums = [100,4,200,1,3,2]
    print(nums)
    r = solution.longestConsecutive(nums)
    print(r)

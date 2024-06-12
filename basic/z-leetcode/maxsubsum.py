from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        #首尾不相连时，和无环的计算方法一样
        #首尾必相连时，j从右到左，依次计算max_sum_start_with[j] = sum(nums[j:n])+maxPrefixSum(nums[0:j-1])
        max_sub_prefix_sum = [0]*n

        maxSubarraySum = nums[0]
        pre_max_sum_end_with = nums[0]
        max_prefix_sum = nums[0]
        prefix_sum = nums[0]
        max_sub_prefix_sum[0] = nums[0]
        for i in range(1,n):
            max_sub_prefix_sum[i] = max(prefix_sum, prefix_sum + nums[i], max_prefix_sum)
            prefix_sum = prefix_sum + nums[i]
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
            pre_max_sum_end_with = max(pre_max_sum_end_with+nums[i], nums[i])
            maxSubarraySum = max(maxSubarraySum, pre_max_sum_end_with)

        right_sum = 0
        for j in range(n-1, 0, -1):
            right_sum = right_sum + nums[j]
            max_sum_start_with = right_sum + max_sub_prefix_sum[j-1]
            maxSubarraySum = max(maxSubarraySum, max_sum_start_with)

        return maxSubarraySum


print(Solution().maxSubarraySumCircular([9,-4,-7,9])) # 18
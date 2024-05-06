class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answers = [1] * n

        product = nums[0]
        for i in range(1, n):
            answers[i] = product
            product *= nums[i]
        
        product = nums[n-1]
        for i in range(n-2, -1, -1):
            answers[i] = answers[i] * product
            product *= nums[i]

        return answers

print(Solution().productExceptSelf([1,2,3,4]))
            
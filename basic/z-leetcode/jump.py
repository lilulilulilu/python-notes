class Solution:
    '''
    判断最少多少步能跳到终点:
    首先第一跳可能的点的下标范围：[1,nums[0]] 能跳到的最远下标max_index = nums[0]
    第二跳可能的点的下标范围：[nums[0]+1,nums[0]+nums[nums[0]]], 计算能跳到的最远下标max_index
    第三跳可能的点的下标范围：[nums[0]+nums[nums[0]]+1,nums[0]+nums[nums[0]]+nums[nums[nums[0]]]]，计算能跳到的最远下标max_index
    
    每次都判断起跳点能跳到的最远距离，一旦超过就是最短跳跃次数，因为首次到达终点的跳数一定是最小的，所以只要找到第一次跳到终点的跳数就是最小跳数。 
    '''
    def jump(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        # 计算从[start，end)区间里的元素能跳达的最远下标max_index
        def maxIndex(nums, start, end):
            max_index = start + nums[start]
            j = start
            while j < end:
                if max_index < j + nums[j]:
                    max_index = j + nums[j]
                j = j + 1
            return max_index

        max_index = nums[0]
        i = 1
        step = 1
        while i <= max_index:
            if max_index >= length-1: # 如果已经超过数组长度，说明跳的步数已经足够了，且是最小跳步。
                return step
            original_max_index = max_index # 保存原值
            max_index = maxIndex(nums, i, original_max_index + 1) # 下一轮检测的终点
            if max_index != original_max_index: # 有改动说明还能有下一轮检测
                step = step + 1
            i = original_max_index + 1 #下一轮检测的起点
        
        return step
    
    
print(Solution().jump([1,2,1,1,1]))

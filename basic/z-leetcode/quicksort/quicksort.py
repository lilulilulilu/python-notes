def quicksort(nums):
    def qk(nums: list[int], start, end) -> None:
        if start >= end:
            return         
        pivot = nums[start]
        i = start
        j = end
        while i < j:
            while i<j and nums[j] > pivot:
                j = j - 1
            nums[i] = nums[j]
            while i<j and nums[i] <= pivot:
                i = i + 1
            nums[j] = nums[i]
        nums[i] = pivot
        qk(nums, start, i-1)
        qk(nums, i+1, end)
    qk(nums, 0, len(nums)-1)
    
nums = [5, 3, 9, 1, 6, 3, 5]
quicksort(nums)
print(nums)

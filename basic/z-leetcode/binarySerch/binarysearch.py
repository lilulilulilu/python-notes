def binarySearch(sortedNums: list[int], target) -> int:
    def bsr(nums, start, end, target) -> int:
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return bsr(nums, start, mid-1, target)
        if nums[mid] < target:
            return bsr(nums, mid+1, end, target)
    return bsr(sortedNums, 0, len(sortedNums)-1, target)



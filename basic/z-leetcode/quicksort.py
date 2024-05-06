def quicksort(nums, left, right):
    # 判断递归终止条件
    if left < 0 or right >= len(nums) or left >= right:
        return
    
    pivot = nums[left]
    i = left
    j = right
    
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
        
    nums[i] = pivot
    
    quicksort(nums, left, i-1)
    quicksort(nums, i+1, right)
              
 
# nums = [3,4,1,2,5]         
# quicksort(nums, 0, len(nums)-1)
# print(nums)

nums =[3, 5, 2, 1, 4]
quicksort(nums, 0, len(nums)-1)
print(nums)
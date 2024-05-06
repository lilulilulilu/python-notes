from quicksort import quicksort

nums = [3,4,1,2,5]
quicksort(nums, 0, len(nums)-1)
print(nums)

def recursiveBinarySearch(nums, start, end, target):
    if start > end: # 递归出口
        return -1
    
    mid = (start + end)//2 # 特殊情况提前返回，省时间
    if nums[mid] == target:
        return mid 
    
    if nums[mid] < target:
        return recursiveBinarySearch(nums, mid+1, end, target)
    if nums[mid] > target:
        return recursiveBinarySearch(nums, start, mid-1, target)
    
    return -1 

def binarySearch(nums, start, end, target):
    i = start 
    j = end
    mid = (start + end)//2
    if nums[mid] == target:
            return mid
    
    while i <= j:    # i，j跳跃步数收敛比线性的查找每次只跳1步要快
        mid = (i+j)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
    return -1
        
        
print(recursiveBinarySearch(nums, 0, len(nums)-1, 1))   
print(binarySearch(nums, 0, len(nums)-1, 1))    
    
print(recursiveBinarySearch(nums, 0, len(nums)-1, 3))    
print(binarySearch(nums, 0, len(nums)-1, 3)) 

print(recursiveBinarySearch(nums, 0, len(nums)-1, 5))   
print(binarySearch(nums, 0, len(nums)-1, 5)) 

print(recursiveBinarySearch(nums, 0, len(nums)-1, 7))   
print(binarySearch(nums, 0, len(nums)-1, 7)) 

  

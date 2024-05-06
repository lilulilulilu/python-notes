from typing import List

class Solution:
    def heapSort(self, nums: List[int]):
        length = len(nums)
        
        # 从最后一个非叶子节点开始，调整堆为大根堆, 此步骤只能保证根节点是最大值，且父节点必然大于子节点
        # 之所以从最后一个非叶子节点开始，是因为最后一个非叶子节点才有可能不是堆。叶子节点不需要调整，因为叶子节点没有子节点
        i = length//2 -1
        while i >= 0:
            self.simpleAdjustHeap(nums, i, length)
            i -= 1
        
        # 将堆顶元素和最后一个元素交换，这样无序长度就减少了1
        while length > 0:
            nums[0], nums[length-1] = nums[length-1], nums[0]
            length = length - 1
            self.simpleAdjustHeap(nums, 0, length)       
        
        
    # 递归方式：i为根节点下标，将i代表的二叉树调整为堆
    def adjustHeap(self, nums: List[int], i: int, length: int ):
        # 递归终止条件
        if i >= length:
            return
        
        # 找到左右子节点中较大的子节点
        left = 2 * i + 1
        right = 2 * i + 2
        larger_child_index = left
        if left < length and right < length and nums[left] < nums[right]:
            larger_child_index = right
        
        # 把较大的子节点的值和父节点的值交换
        if larger_child_index < length and nums[larger_child_index] > nums[i]:
            nums[larger_child_index], nums[i] = nums[i], nums[larger_child_index]
            # 交换后的子节点为根的堆可能不是大根堆了，所以继续调整子树为大根堆 
            self.adjustHeap(nums, larger_child_index, length)
    
    # 循环方式：i为根节点下标，将i代表的二叉树调整为堆  
    # 前置条件：i的左右子树都是大根堆    
    def simpleAdjustHeap(self, nums: List[int], i: int, length: int ):
        while i < length:
            # 找到左右子节点中较大的子节点
            left = 2 * i + 1
            right = 2 * i + 2
            larger_child_index = left
            if left < length and right < length and nums[left] < nums[right]:
                larger_child_index = right
        
            # 把较大的子节点的值和父节点的值交换
            if larger_child_index < length and nums[larger_child_index] > nums[i]:
                nums[larger_child_index], nums[i] = nums[i], nums[larger_child_index]
            # 交换后的子节点为根的堆可能不是大根堆了，所以继续调整子树为大根堆 
            i = larger_child_index
            
nums = [3,2,1,5,6,4,7,3,3,3,3]  
Solution().heapSort(nums)
print(nums)

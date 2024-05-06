from typing import List
class Solution:
    def findKthLargestWithQuickSort(self, nums: List[int], k: int) -> int:
            if len(nums) == 0:
                return 0

            pivot = nums[0]
            smaller = []
            bigger = []
            equal = []

            length = len(nums)
            for i in range(length)[1:] :
                if nums[i] < pivot:
                    smaller.append(nums[i])
                if nums[i] > pivot:
                    bigger.append(nums[i])
                if nums[i] == pivot:
                    equal.append(nums[i])

            bigger_len = len(bigger)
            if bigger_len == k-1 :
                return pivot
            if bigger_len > k-1:
                return self.findKthLargest(bigger, k)
            if bigger_len < k-1:
                if len(equal) + bigger_len >= k-1:
                    return pivot
                return self.findKthLargest(smaller + equal, k - bigger_len - 1)

    def findKthLargestWithHeapSort(self, nums: List[int], k: int) -> int:

        length = len(nums)
        
        # 从最后一个非叶子节点开始，调整堆为大根堆, 此步骤只能保证根节点是最大值，且父节点必然大于子节点
        i = length//2 -1
        while i >= 0:
            self.adjustHeap(nums, i, length)
            i -= 1
        
        # 将堆顶元素和最后一个元素交换，这样无序长度就减少了1, j=k，每次取出一个最大值就将j减1
        j = k 
        while length > 0 and j > 0:
            nums[0], nums[length-1] = nums[length-1], nums[0]
            length = length - 1
            j = j - 1
            self.adjustHeap(nums, 0, length)  
            
        # 返回第k大的值         
        return nums[len(nums)- k]     
        
        
    # i为根节点下标，将i代表的二叉树调整为堆
    def adjustHeap(self, nums: List[int], i: int, length: int ):
        if i >= length:
            return
        
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

    
    # i为根节点下标，将i代表的二叉树调整为堆
    def simpleAdjustHeap(self, nums: List[int], i: int, length: int ):
        while i < length:
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


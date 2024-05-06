from .main1 import f1
from leetcode.quicksort import quicksort

if __name__ == "__main__":
    f1()
    print("main")
    nums = [3, 5, 2, 1, 4]
    quicksort(nums, 0, len(nums)-1)
    print(nums)
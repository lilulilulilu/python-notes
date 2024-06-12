'''
题目： 一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ"（2 26）、"VF"（22 6）或者 "BBF"（2 2 6）。
'''
def nums_decode(nums: str) -> int:
    n = len(nums)
    if n <= 1:
        return 1

    j = n-1
    if nums[j] == '0':
        return nums_decode(nums[0: j-1])
    elif 1 <= int(nums[j-1:j+1]) <= 26:
        a = nums_decode(nums[0: j-1]) # 2 character
        b = nums_decode(nums[0: j]) # 1character
        return a + b
    else:
        return nums_decode(nums[0: j])
    
print(nums_decode('12'))  # 2
print(nums_decode('226'))  # 3


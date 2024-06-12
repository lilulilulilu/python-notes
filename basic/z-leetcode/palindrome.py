class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s

        def get_palindrome_max_length(center, s):
            i, j = center 
            length = 0
            while j+length < n and i-length >= 0:
                if s[j+length] == s[i-length]:
                    length = length + 1
                else:
                    break    
            return length

        center = (-1, -1)
        max_len = -1
        for i in range(n):
            temp_center = (i, i)
            length = get_palindrome_max_length(temp_center, s)
            if length > max_len:
                max_len = length
                center = temp_center
            temp_center = (i, i+1)
            length = get_palindrome_max_length(temp_center, s)
            if length >= max_len:
                max_len = length
                center = temp_center

        return s[center[0]-max_len+1: center[1]+max_len]

print(Solution().longestPalindrome("cbbd"))
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        minW = len(s) + 1
        start = -1

        if n1 < n2:
            return ""
        
        s_mp = Counter(s)
        if n1 == n2:
            if s_mp == Counter(t):
                return s
            else:
                return ""

        def isContain(s2:str, t:str) -> bool:
            if len(s2) == 0:
                return False
            s2_mp = Counter(s2)
            t_mp = Counter(t)
            for k, v in t_mp.items():
                if k not in s2_mp:
                    return False
                elif k in s2_mp and s2_mp[k] < v:
                    return False
            return True
        
        i = 0
        j = n2
        while i <= j and j <= n1:
            if isContain(s[i:j], t):
                if minW >= j-i:
                    minW = j-i
                    start = i
                i = i + 1
            else:
                j = j + 1
                
        if start == -1:
            return ""
        
        return s[start: start+minW]

print(Solution().minWindow("ab",  "A"))
# print(Solution().minWindow("ADOBECODEBANC",  "ABC"))
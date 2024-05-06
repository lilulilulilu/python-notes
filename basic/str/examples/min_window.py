from collections import deque, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特殊情况提前返回
        if len(t) > len(s):
            return ""
            
        if len(s) == len(t):
            if Counter(s) == Counter(t):
                return s
            else:
                return ""

        indexQ = deque() # 存放起始比较下标
        tcharS = [c for c in t] # 元素放入列表，因为可能有重复值，方便查找和删除
        minL = len(s) + 1
        start = -1
        
        for i in range(len(s)):
            if s[i] in tcharS:
                indexQ.append(i)
                
        print("len(indexQ)", len(indexQ))
        
        while indexQ:
            index = indexQ.popleft()
            tempS = tcharS.copy()
            count = 1 
            tempS.remove(s[index])
            if len(tempS) == 0:
                if minL >= count:
                    minL = count
                    start = index
            if index + len(t) > len(s):
                continue
            j = index + 1
            while j < len(s):
                count += 1
                if s[j] in tempS:
                    tempS.remove(s[j])
                    if len(tempS) == 0:
                        if minL >= count:
                            minL = count
                            start = j - minL + 1
                j += 1


        if start == -1:
            return ""
        return s[start: start + minL]
 
 
 
    def minWindow2(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        minW = len(s) + 1
        start = -1

        if n1 < n2:
            return ""
        
        s_mp = Counter(s)
        t_mp = Counter(t)
        if n1 == n2:
            if s_mp == t_mp:
                return s
            else:
                return ""

        def isContain(s2:str, t_mp: dict) -> bool:
            if len(s2) == 0 or len(s2) < len(t_mp):
                return False
            s2_mp = Counter(s2)
            for k, v in t_mp.items():
                if k not in s2_mp:
                    return False
                elif k in s2_mp and s2_mp[k] < v:
                    return False
            return True

        indexQ = deque()
        for i in range(n1):
            if s[i] in t_mp:
                indexQ.append(i)

        print("len(indexQ)", len(indexQ))

        while indexQ:
            i = indexQ.popleft()
            j = i + n2
            while i <= j and j <= n1:
                if isContain(s[i:j], t_mp):
                    if minW >= j-i:
                        minW = j-i
                        start = i
                    i = i + 1
                else:
                    j = j + 1

        if start == -1:
            return ""

        return s[start: start+minW]
        
# print(Solution().minWindow("bbaa", "aba"))
# print(len("cabccbbcbabaccccbcccbbbbacccccbbbabababc"))
# print(Solution().minWindow("cabccbbcbabaccccbcccbbbbacccccbbbabababc", "bcabaabbaaaca"))



                






        
    

        

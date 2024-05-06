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
        
# print(Solution().minWindow("bbaa", "aba"))
# print(len("cabccbbcbabaccccbcccbbbbacccccbbbabababc"))
print(Solution().minWindow("cabccbbcbabaccccbcccbbbbacccccbbbabababc", "bcabaabbaaaca"))



                






        
    

        

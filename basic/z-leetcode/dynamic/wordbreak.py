from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if s.startswith(word):
                m = len(word)
                if m == len(s):
                    return True
                exist = self.wordBreak(s[m:], wordDict)
                if exist:
                    return True
        return False
                
                
                
                
print(Solution().wordBreak("leetcode", ["leet", "code"])) # True
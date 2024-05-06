class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = [item.strip() for item in s.split()]

        if len(pattern) != len(s_arr):
            return False
        
        pd = {} # key 是pattern里的字符
        sd = {} # key 是s里的单词word
        for c, w in zip(pattern, s_arr):
            if (c in pd and pd[c] != w) or (w in sd and sd[w] != c):
                return False
            if c not in pd:
                pd[c] = w
            if w not in sd:
                sd[w] = c

        return True

print(Solution().wordPattern("abba", "dog cat cat dog"))
class Solution:
    def calculate(self, s: str) -> int:
        if s.isdigit():
            return int(s)

        s = s.replace(' ', '')
        n = len(s)

        nums = []
        sign = '+'
        i = 0
        while i < n:
            if s[i].isdigit():
                if i == 0:
                    nums.append(int(s[i]))
                    i = i + 1
                    continue
                if sign == '+': 
                    if s[i-1] == '+' or s[i-1] == '(':
                        nums.append(int(s[i]))
                    elif s[i-1] == '-':
                        nums.append(-int(s[i]))
                elif sign == '-':           
                    if s[i-1] == '-':
                        nums.append(int(s[i]))
                    elif s[i-1] == '+' or s[i-1] == '(':
                        nums.append(-int(s[i]))   
            if s[i] == '(':
                if i-1 >= 0 and s[i-1] == '-':
                    sign = '-'
            if s[i] == ')':
                total = sum(nums)
                nums = [total]
                sign = '+'
            i = i + 1

        return sum(nums)    
            

print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")) # 2


        
            

        








       

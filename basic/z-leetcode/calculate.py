import re
class Solution:
    def calculate(self, s: str) -> int:
        if s.isdigit():
            return int(s)
        
        s = s.replace(' ', '')
        n = len(s)
        i = 0
        start = -1
        end = n
        while i < n:
            if s[i] == '(':
                start = i
            elif s[i] == ')':
                end = i
                break
            i = i + 1

        def compute(exp_str) -> int:
            exp = re.findall(r'\d+|[+-]', exp_str)
            nums = []
            i = 0
            while i < len(exp):
                if exp[i] == '-':
                    nums.append(-int(exp[i+1]))
                    i = i + 2
                elif exp[i] == '+':
                    nums.append(int(exp[i+1]))
                    i = i + 2
                else:
                    nums.append(int(exp[i]))
                    i = i + 1
            return sum(nums)

        if start + 1 < n:          
            exp_str = s[start+1:end]
            num = compute(exp_str)
            if start == -1:
                return num
            else:
                new_exp_str = s[0:start] + str(num)
                if end+1 < n:
                    new_exp_str = new_exp_str + s[end+1:n]
                new_exp_str = new_exp_str.replace('--', '+')
                new_exp_str = new_exp_str.replace('+-', '-')
                return self.calculate(new_exp_str)
        
            

print(Solution().calculate("1-(2+3-(4+(5-(1-(2+4-(5+6))))))"))      








       

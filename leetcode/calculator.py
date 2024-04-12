import re

class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub(r' +', '', s)
        #去掉首尾的()
        l = len(s)
        if l > 2 and s[0] == '(' and s[-1] == ')' and s[1:l-1].isdigit():
            return int(s[1:l-1])

        # 递归出口：如果是纯数字字符串，则直接返回
        if s.isdigit():
            return int(s)
        
        # 如果是数字开头，则找到第一个数字，后面的递归计算
        # 如果不是数字开头，则找到反符号，然后切割字符串，使用递归计算总值
        i = 0
        l = len(s)
        if s[0].isdigit():
            while s[i].isdigit():
                i += 1
            a = self.calculate(s[0:i])
            operator = s[i]
            b = self.calculate(s[i+1:])
            return self.process(a ,operator, b)
        else:
            k = 0
            while i < l:
                if s[i] == '(':
                    k += 1
                    i += 1
                    continue
                elif s[i] == ')':
                    k -= 1
                    i += 1
                    if k == 0:
                        if i < l:
                            a = self.calculate(s[0:i])
                            operator = s[i]
                            b = self.calculate(s[i+1:])
                            if operator == '-':
                                operator = '+'
                                b = -b
                            return self.process(a ,operator, b)
                        else:
                            start = 1
                            end = len(s)-1
                            return self.calculate(s[start:end])
                else:
                    i += 1

    def process(self, a, operator, b) -> int:
        operatorMap = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: a/b,
        }
        return int(operatorMap[operator](a,b))


if __name__ == '__main__':
    solution = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    s = " 2-1 + 2 "
    r = solution.calculate(s)
    print(r)

 

     
            




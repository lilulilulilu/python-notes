from typing import List
class Solution:
    def isNumber(self, e: str) -> bool:
        return e.isdigit()
    
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for e in tokens:
            if self.isNumber(e):
                s.append(e)
            elif self.isOperator(e):
                a = s.pop()
                b = s.pop()
                result = self.compute(b,a,e)
                s.append(result)
        return int(s.pop())

    def isOperator(self, e: str) -> bool:
        return e in ['+', "-", "*", "/"]

    def compute(self, a: str, b: str, o: str) -> str:
        operatorMap = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: a / b
        }
        a = int(a)
        b = int(b)
        return operatorMap[o](a, b)
    
    def process2(self, a: str, b: str, e: str) -> str:
        a = int(a)
        b = int(b)
        if e == '+':
            return a + b
        if e == '-':
            return a - b
        if e == '*':
            return a * b
        if e == '/':
            return a / b
        
if __name__ == '__main__':
    solution = Solution()
    tokens = ["4","13","5","/","+"]
    r = solution.evalRPN(tokens)
    print(r)
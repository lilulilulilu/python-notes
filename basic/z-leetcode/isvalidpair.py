class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['{','(', '[']
        closeBrackets = ['}',')', ']']
        stack = []
        for e in s:
            if e in openBrackets:
                stack.append(e)
            elif e in closeBrackets:
                if len(stack) <= 0:
                    return False
                popE = stack.pop()
                if not self.isPair(popE, e):
                    return False
                
        return not stack
    
    def isValid2(self, s: str) -> bool:
        bracketMap = {'{':'}', '(':')', '[':']'}

        stack = []
        for e in s:
            if e in bracketMap:
                stack.append(e)
            else :
                if len(stack) == 0:
                    return False
                topE = stack.pop()
                if e != bracketMap[topE]:
                    return False
                
        return not stack          
                    
    def isPair(self, openC, closeC) -> bool:
        if openC == '{' and closeC == '}':
            return True
        if openC == '(' and closeC == ')':
            return True
        if openC == '[' and closeC == ']':
            return True
        return False
    
    def isPair2(self, openC, closeC) -> bool:
        bracketMap = {'{':'}', '(':')', '[':']'}
        return closeC == bracketMap[openC]

    
            
if __name__ == '__main__':
    solution = Solution()
    s = "()"
    r = solution.isValid2(s)
    print(r)
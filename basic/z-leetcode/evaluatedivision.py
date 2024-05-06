from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = {}
        n = len(equations)

        def sorted_str(s: str) -> float:
            return "".join(sorted(s, key=lambda x:ord(x)))

        def isSame(x1,x2) -> bool:
            if len(x1) != len(x2):
                return False
            sorted_x1 = sorted_str(x1)
            sorted_x2 = sorted_str(x2)
            if sorted_x1 == sorted_x2:
                return True
            else:
                return False

        def simple(equation: List[str]) -> list[str]:
            x1, x2 = equation
            for c in x1:
                if c in x2:
                    x1 = x1.replace(c, "", 1)
                    x2 = x2.replace(c, "", 1)
            if x1 == "":
                x1 = "1"
            if x2 == "":
                x2 = "1"
            return [sorted_str(x1), sorted_str(x2)]

        def extract_lower(s: str) -> list[str]:
            return {c for c in s if c.islower()}

        characters = extract_lower(str(equations))

        for i in range(n):
            if not isSame(equations[i][0], equations[i][1]):
                x1, x2 = simple(equations[i])
                d[(x1,x2)] = values[i]
                d[(x2,x1)] = 1/values[i]
                d[(x1,x1)] = 1
                d[(x2,x2)] = 1
                if [x1, x2] not in equations:
                    equations.append([x1, x2])
                if [x2, x1] not in equations:
                    equations.append([x2, x1])  

        print("d", d)      
        
        while equations:
            x1, x2 = simple(equations.pop())
            for i in range(len(equations)):
                x3, x4 = simple(equations[i])
                if x3 == x2 and x1 != x4:
                    if (x1, x4) not in d:
                        d[(x1,x4)] = d[(x1, x2)] * d[(x3, x4)]
                        if [x1, x4] not in equations:
                            equations.append([x1, x4])
                if x1 == x4 and x3 != x2:
                    if (x3, x2) not in d:
                        d[(x3,x2)] = d[(x3, x4)] * d[(x1, x2)]
                        if [x3, x2] not in equations:
                            equations.append([x3,x2])
        
        def get_value(equation) -> float:
            if isSame(equation[0], equation[1]):
                i = 0
                for c in equation[0]:
                    if c in characters:
                        i += 1
                if i == len(equation[0]):
                    return 1
                else:
                    return -1

            x1, x2 = simple(equation)
            k = (x1, x2)
            if k in d:
                return d[k]
            else:
                return -1

        return [get_value(e) for e in queries]
        
equations = [["a","aa"]]
values = [9.0]
print(Solution().calcEquation(equations, values, [["aa","a"],["aa","aa"]]))


           
# equations = [["a","b"],["b","c"]]s
# values = [2.0,3.0]
# print(Solution().calcEquation(equations, values, [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))



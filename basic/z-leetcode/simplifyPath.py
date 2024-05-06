import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r'/+', '/', path)
        parts = path.split('/')

        stack = []
        # 遍历parts中的每个元素，如果等于..则要退回上一个目录
        for p in parts:
            if p!='' and p != '..' and p != '.':
                stack.append(p)
            elif len(stack)!=0 and p == '..':
                stack.pop()

        return '/' + '/'.join(stack)
    
if __name__ == '__main__':
    solution = Solution()
    s = "/home/"
    s = "/a/./b/../../c/"
    r = solution.simplifyPath(s)
    print(r)
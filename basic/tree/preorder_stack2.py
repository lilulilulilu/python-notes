# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root and root.left is None and root.right is None:
            return [root.val]
            
        preoder = []
        q = deque()
        q.append(root)
        preoder.append(root.val)
        visited = set()
        visited.add(root)
        while q:
            p = q[-1]
            if (p.left is None or p.left in visited) and (p.right is None or p.right in visited):
                q.pop()
            while p.left and p.left not in visited:
                q.append(p.left)
                visited.add(p.left)
                preoder.append(p.left.val)
                p = p.left
            if p.right and p.right not in visited:
                q.append(p.right)
                visited.add(p.right)
                preoder.append(p.right.val)
        return preoder
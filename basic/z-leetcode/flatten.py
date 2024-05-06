# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        if root.left is None and root.right is None:
            return 
        
        left = root.left
        right = root.right
        
        root.left = None
        root.right = None

        flatten_left = None
        flatten_right = None
        if left:
            self.flatten(left)
            flatten_left = left
        if right:
            self.flatten(right)
            flatten_right = right

        if flatten_left:
            root.right = flatten_left
        if flatten_right:
            p = root
            print("root:",p.val)
            while p.right:
                print(p.val)
                p = p.right
            p.right = flatten_right
            
node1 = TreeNode(1)
node2 = TreeNode(2)
node5 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node6 = TreeNode(6)

node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.right = node6

Solution().flatten(node1)

p = node1
while p:
    print(p.val)
    p = p.right





            

         
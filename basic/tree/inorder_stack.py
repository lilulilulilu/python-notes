class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    # Use a stack to track nodes and a current pointer to traverse the tree.
    # The basic idea is to push all the left children onto the stack until you can't anymore,
    # then pop from the stack, process the node's value, and move to its right subtree.
    result, stack = [], []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)  # Add the node's value
        current = current.right  # Switch to right subtree
    
    return result

# Example Usage
# Constructing a binary tree as follows:
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Expected output: [1, 3, 2] - The inorder traversal of the tree
print(inorder_traversal(root))

# 使用栈来追踪节点并使用当前指针遍历树。
# 基本思想是将所有左孩子推入栈中，直到不可能为止，
# 然后从栈中弹出，处理节点的值，然后转移到其右子树。

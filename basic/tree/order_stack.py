# The non-recursive implementation of postorder traversal for a binary tree involves using a stack.
# The idea is to use two stacks. The first stack is used to perform a modified preorder traversal (root, right, left)
# and the second stack is used to store the nodes in postorder.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if not root:
        return []
    result = []
    stack = [root] 
    while  stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    result = reversed(result)
    return result

# 先序遍历也是深度优先的思想
def preorderTraversal(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorder_traversal(root):
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
    # Use a stack to track nodes and a current pointer to traverse the tree.
    # The basic idea is to push all the left children onto the stack until you can't anymore,
    # then pop from the stack, process the node's value, and move to its right subtree.

# Test case
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(postorderTraversal(root))  # Output: [3, 2, 1]

# 通过使用两个栈，实现了二叉树的后序遍历。首先，使用第一个栈按照root-right-left的顺序进行遍历，并将结果存入第二个栈。
# 最后，从第二个栈中依次取出节点值，即得到了后序遍历的结果。

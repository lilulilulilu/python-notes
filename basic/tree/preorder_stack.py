# Preorder traversal of binary tree using a non-recursive approach
# The idea is to use a stack to keep track of nodes. We start by pushing the root node onto the stack.
# While the stack is not empty, we pop a node, process it (visit it), and push its right child first, then its left child to the stack.
# This way, since the stack is LIFO, the left child is processed before the right child, maintaining the 'root -> left -> right' order of preorder traversal.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# Example to test the non-recursive preorder traversal
if __name__ == '__main__':
    # Creating a binary tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(preorderTraversal(root))  # Output: [1, 2, 4, 5, 3]

# 使用非递归方法实现二叉树的先序遍历。
# 思路是使用一个栈来跟踪节点。开始时将根节点推入栈。
# 当栈不为空时，弹出一个节点，处理它（访问它），然后先将其右子节点压入栈，再将其左子节点压入栈。
# 由于栈是后进先出的，这样可以保证先处理左子节点再处理右子节点，从而维持先序遍历的“根左右”顺序。

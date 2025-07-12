# leetcode 226
# Given the root of a binary tree, invert the tree, and return its root.
from idlelib.tree import TreeNode


# Time Complexity:
# Space Complexity:

def invertBinaryTree(self, node: TreeNode) -> TreeNode:
    if not node:
        return

    left_child = node.left
    right_child = node.right

    node.left = right_child
    node.right = left_child

    self.invertTree(node.left)
    self.invertTree(node.right)

    return node

print(invertBinaryTree([4,2,7,1,3,6,9]))
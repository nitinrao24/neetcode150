# leetcode 543
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: TreeNode):
            nonlocal diameter

            if node is None:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            path_length = left_depth + right_depth
            if path_length > diameter:
                diameter = path_length

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return diameter
print(Solution().diameterOfBinaryTree([1,2,3,4,5]))

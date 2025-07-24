# leetcode 110
# Given a binary tree, determine if it is height-balanced.
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                balanced = True
                height = 0
                return balanced, height

            left_result = dfs(node.left)
            left_balanced = left_result[0]
            left_height = left_result[1]

            right_result = dfs(node.right)
            right_balanced = right_result[0]
            right_height = right_result[1]

            # calculate current height
            if left_height > right_height:
                height = left_height + 1
            else:
                height = right_height + 1

            # calculate height difference
            diff = left_height - right_height
            if diff < 0:
                diff = -diff

            # see if its balanced
            balanced = left_balanced and right_balanced and diff <= 1

            return balanced, height

        dfs_result = dfs(root)
        result = dfs_result[0]
        return result
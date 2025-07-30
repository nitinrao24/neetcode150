# leetcode 124
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
# has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# Time Complexity:
# Space Complexity:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(node):
            nonlocal max_sum

            if node is None:
                return 0

            left_gain = dfs(node.left)
            if left_gain < 0:
                left_gain = 0

            right_gain = dfs(node.right)
            if right_gain < 0:
                right_gain = 0

            current_sum = node.val + left_gain + right_gain
            if current_sum > max_sum:
                max_sum = current_sum

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
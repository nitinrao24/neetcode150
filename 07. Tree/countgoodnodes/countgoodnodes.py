# leetcode 1448
# Given a binary tree root,
# a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
from typing import List
from typing import Optional
import collections
from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if node is None:
                return 0

            if node.val >= current_max:
                count = 1
            else:
                count = 0

            if node.val > current_max:
                next_max = node.val
            else:
                next_max = current_max

            left_count = dfs(node.left, next_max)
            right_count = dfs(node.right, next_max)

            total = count + left_count + right_count
            return total

        result = dfs(root, root.val)
        return result

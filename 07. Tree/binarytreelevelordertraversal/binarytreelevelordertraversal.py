# leetcode 102
# Given the root of a binary tree,
# return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
import collections
# Time Complexity:
# Space Complexity:
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels.append(level)

        return levels
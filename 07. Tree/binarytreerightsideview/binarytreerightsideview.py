# leetcode 199
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
from typing import List
from typing import Optional
import collections
from collections import deque
# Time Complexity:
# Space Complexity:
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            rightmost_node = None

            level_length = len(queue)
            for _ in range(level_length):
                current_node = queue.popleft()
                if current_node:
                    rightmost_node = current_node
                    queue.append(current_node.left)
                    queue.append(current_node.right)

            if rightmost_node:
                result.append(rightmost_node.val)

        return result

# leetcode 230
# Given the root of a binary search tree,
# and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()

            count += 1
            if count == k:
                return node.val

            node = node.right
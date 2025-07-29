# leetcode 98
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
from typing import Optional
from typing import List
import collections
from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if node is None:
                return True

            value = node.val
            if value <= low or value >= high:
                return False

            left_is_valid = validate(node.left, low, value)
            right_is_valid = validate(node.right, value, high)

            return left_is_valid and right_is_valid

        result = validate(root, float("-inf"), float("inf"))
        return result
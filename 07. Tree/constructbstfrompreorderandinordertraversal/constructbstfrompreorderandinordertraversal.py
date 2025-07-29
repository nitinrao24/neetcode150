# leetcode 105
# Given two integer arrays preorder and inorder where preorder is the preorder traversal
# of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_queue = deque(preorder)

        def build(pre_queue, in_list):
            if not in_list:
                return None

            root_val = pre_queue.popleft()
            split_index = in_list.index(root_val)

            node = TreeNode(root_val)

            left_in_list = in_list[:split_index]
            right_in_list = in_list[split_index + 1:]

            node.left = build(pre_queue, left_in_list)
            node.right = build(pre_queue, right_in_list)

            return node

        result = build(pre_queue, inorder)
        return result
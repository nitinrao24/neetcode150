# leetcode 235
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
# and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        node1 = p
        node2 = q

        while node:
            val = node.val

            if node1.val > val and node2.val > val:
                node = node.right
            elif node1.val < val and node2.val < val:
                node = node.left
            else:
                return node

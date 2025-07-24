# leetcode 572
# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            left_same = is_same_tree(node1.left, node2.left)
            right_same = is_same_tree(node1.right, node2.right)
            return left_same and right_same

        def search(node):
            if node is None:
                return False

            if is_same_tree(node, subRoot):
                return True

            found_left = search(node.left)
            found_right = search(node.right)
            return found_left or found_right

        return search(root)
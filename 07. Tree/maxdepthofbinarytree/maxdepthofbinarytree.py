# leetcode 104
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# Time Complexity:
# Space Complexity:

def maxDepthOfBinaryTree(self,root):
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

print(maxDepthOfBinaryTree([1,2]))
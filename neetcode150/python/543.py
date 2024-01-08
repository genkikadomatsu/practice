"""543"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = 0

        def maxDepth(node):

            if not node:
                return -1

            left_depth = 1 + self.diameterOfBinaryTree(node.left)
            right_depth = 1 + self.diameterOfBinaryTree(node.right)

            nonlocal max_diameter 
            max_diameter = max(max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) 

        maxDepth(root)

        return max_diameter
from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        flattened = []

        def inorder(root):
             
            if not root:
                return 0
            
            recurse(root.left)
            flattened.append(root.val)            
            recurse(root.right)

        inorder(root)
        return flattened[k - 1]
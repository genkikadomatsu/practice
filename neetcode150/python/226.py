"""226"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        if root.left and root.right:
            root.right, root.left = root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
            return root

        if root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
            return root
    
        if root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
            return root

        return root
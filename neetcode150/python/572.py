"""572"""
from re import sub
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Empty tree is sub-tree of all trees
        if bool(root) ^ bool(subRoot):
            return False

        # Empty tree is a sub-tree of an empty tree
        if not root and not subRoot:
            return True

        # Both are non-empty, then check if values match and recurse 
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, a, b):
        
        # If either is None, not same tree
        if bool(a) ^ bool(b):
            return False

        # If both are None, same 
        if not (a or b):
            return True

        # Recurse on subtrees
        if a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
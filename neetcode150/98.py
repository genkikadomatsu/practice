from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(node, min_bound, max_bound):
            return ((not node)
                    or ((min_bound < node.val < max_bound)
                        and (not (node.left and node.left.val > node.val))
                        and (not (node.right and node.val > node.right.val))
                        and (recurse(node.left, min_bound, node.val)
                            and recurse(node.right, node.val, max_bound))))
        
        return recurse(root, float("-inf"), float("inf")) 
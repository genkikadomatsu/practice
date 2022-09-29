# LeetCode 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# given two tree roots, p and q, determine if the trees are the same

class Solution:

    def isSameTree(self, p, q) -> bool:

        # cut-off cases

        # false: one has value and one doesn't or the values don't match
        if (not p and q) or (p and not q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

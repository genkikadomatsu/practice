
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recurse(node, max) -> int:
            
            if not node:
                return 0

            if node.val >= max:
                max = node.val
                return 1 + recurse(node.right, max) + recurse(node.left, max)    
        
            return recurse(node.right, max) + recurse(node.left, max)

        return recurse(root, root.val) 
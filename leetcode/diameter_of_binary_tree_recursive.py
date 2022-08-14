# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        max_diam = 0

        def max_height(node):
            
            nonlocal max_diam

            if not node:
                return 0
            
            left_height = max_height(node.left)
            right_height = max_height(node.right)
            max_diam = max(max_diam, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        max_height(root)
        return max_diam
# Examples
#  
#      /\
#     /
#    /\
#   /  \
#  /    \
# /      \
# This has a diameter of 8, a subtree could potentially have a

# Leaf Nodes
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

# L2 Nodes
node2 = TreeNode(2, node1, node3)
node7 = TreeNode(7, node6, node9)

# Root Node
node4 = TreeNode(4, node2, node7)

sol = Solution()
print(sol.diameterOfBinaryTree(node4))

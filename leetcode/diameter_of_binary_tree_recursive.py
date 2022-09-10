# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        max_diam = 0
        
        def recurse(root):

            nonlocal max_diam

            if not root: return -1

            left_depth = 1 + recurse(root.left)
            
            right_depth = 1 + recurse(root.right)
            print("Root ", root.val, "Left Depth ", left_depth, "Right Depth ", right_depth)
            diam = left_depth + right_depth
            if diam > max_diam: max_diam = diam
            return max(left_depth, right_depth)
            
        
        recurse(root)
        return max_diam

# Examples
#             1
#            / \
#           2   3
#          /
#         4
#        / \
#       5   6
#      /     \
#     7       8 
#    /         \
#   9          10
#  /             \
# 11             12
#
# Diameter of 8 not 7

# Test 1
node11 = TreeNode(11)
node12 = TreeNode(12)

node9 = TreeNode(9, left=node11)
node10 = TreeNode(10, right=node12)

node7 = TreeNode(7, left=node9)
node8 = TreeNode(8, right=node10)

node5 = TreeNode(5, left=node7)
node6 = TreeNode(6, right=node8)

node4 = TreeNode(4, node5, node6)

node2 = TreeNode(2, left=node4)
node3 = TreeNode(3)

node1 = TreeNode(1, left=node2, right=node3)


# Test 2
# node3 = TreeNode(3)
# node2 = TreeNode(2)
# node1 = TreeNode(1, left=node2, right=node3)


sol = Solution()
print(sol.diameterOfBinaryTree(node1))

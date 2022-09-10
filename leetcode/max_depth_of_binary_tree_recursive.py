# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root.left and root.right:
            return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        elif root.left:
            return 1 + self.maxDepth(root.left)
        elif root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1


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
print(sol.maxDepth(node4))

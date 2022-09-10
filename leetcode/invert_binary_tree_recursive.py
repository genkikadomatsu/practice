# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        print('Inverting Tree')

        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        
        return root

# Number of Submissions:


# Testing Stuff

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
sol.invertTree(node4)



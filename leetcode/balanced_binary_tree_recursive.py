# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        result = True

        def recursion(node) -> int:
            print('recursing')
            nonlocal result
            if result == False: return 0

            if not node: return -1
            
            left_depth = 1 + recursion(node.left)
            right_depth = 1 + recursion(node.right)

            if abs(left_depth - right_depth) > 1:
                result = False
            
            return max(left_depth, right_depth)
            
        recursion(root)
        return result



# Test 1
node5 = TreeNode(5)
node6 = TreeNode(6)

node4 = TreeNode(4, left=node5)

node2 = TreeNode(2, left=node4)
node3 = TreeNode(3)

node1 = TreeNode(1, left=node2, right=node3)


# Test 2
# node3 = TreeNode(3)
# node2 = TreeNode(2)
# node1 = TreeNode(1, left=node2, right=node3)


sol = Solution()
print(sol.isBalanced(node1))

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NeetCodeSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = preorder[0]
        root_i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_i + 1], inorder[:root_i])
        root.right = self.buildTree(preorder[root_i + 1:], inorder[root_i:])
        return root        


class NaiveSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode | None:
        
        if not preorder or not inorder:
            return None

        # Construct the root, as preorder[0] is always the root
        subtree_root = TreeNode(preorder[0])
        
        # Find the root index, aka the 'pivot' 
        subtree_root_inorder_i = inorder.index(subtree_root.val)

        # Construct sublists using the pivot 
        preorder_left_subtree = preorder[1:subtree_root_inorder_i + 1]
        preorder_right_subtree = preorder[subtree_root_inorder_i + 1:]
        inorder_left_subtree = inorder[:subtree_root_inorder_i]
        inorder_right_subtree = inorder[subtree_root_inorder_i + 1:]

        # Make recurisve calls for the left and right subtree using the sublists 
        recursive_call = lambda preord, inord: self.buildTree(preord, inord)
        subtree_root.left = recursive_call(preorder_left_subtree, inorder_left_subtree)
        subtree_root.rght = recursive_call(preorder_right_subtree, inorder_right_subtree)

        return subtree_root


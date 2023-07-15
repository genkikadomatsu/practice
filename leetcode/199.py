# LeetCode 199

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
 
        if not root:
            return root
       
        result = []
        queue = deque([root])

        while queue:
            result.append(queue[-1].val)
            
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
               
                if node.right:
                    queue.append(node.right)

        return result
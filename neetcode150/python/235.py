class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return self.lowestCommonAncestor(root.left, p, q)
 
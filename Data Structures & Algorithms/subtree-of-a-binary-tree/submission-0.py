# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and subRoot:
            return False
        if root and not subRoot:
            return False

        if self.same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def same(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        
        if subRoot and root is None:
            return False
        if root and subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return self.same(root.left, subRoot.left) and self.same(root.right, subRoot.right)









      
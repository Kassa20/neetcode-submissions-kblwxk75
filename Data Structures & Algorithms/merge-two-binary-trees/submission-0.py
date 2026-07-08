# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return None

            node = TreeNode()

            if not root2:
                node.val = root1.val
                node.left = dfs(root1.left, root2)
                node.right = dfs(root1.right, root2)

            elif not root1:
                node.val = root2.val    
                node.left = dfs(root1, root2.left)
                node.right = dfs(root1, root2.right)

            else:
                node.val = root1.val + root2.val
                node.left = dfs(root1.left, root2.left)
                node.right = dfs(root1.right, root2.right)

            return node


        return dfs(root1, root2)




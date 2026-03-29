# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return []

        good = 1
        def dfs(root, m):
            nonlocal good
            if not root:
                return None

            if root.val >= m:
                good += 1
            m = max(m, root.val)

            dfs(root.left, m)
            dfs(root.right, m)

        dfs(root.left, root.val)
        dfs(root.right, root.val)


        return good









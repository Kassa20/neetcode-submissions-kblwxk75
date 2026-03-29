# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, m):
            if not root:
                return 0

            res = 1 if root.val >= m else 0
            m = max(m, root.val)

            res += dfs(root.left, m)
            res += dfs(root.right, m)
            return res

        return dfs(root, root.val)








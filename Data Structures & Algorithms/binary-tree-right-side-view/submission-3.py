# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        res = []
        levels = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    continue
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            
            levels.append(level)
        
        for level in levels:
            if len(level) == 0:
                continue           
            if len(level) == 1:
                res.append(level[0])
            else:
                res.append(level[-1])
            
        return res












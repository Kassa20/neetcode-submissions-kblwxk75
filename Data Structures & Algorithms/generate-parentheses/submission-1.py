class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(op, cl, s):

            if op > n or cl > n:
                return

            if cl > op:
                return

            if cl == n and op == n:
                res.append(s)
                return

            dfs(op + 1, cl, s + "(")
            dfs(op, cl + 1, s + ")")


        dfs(1, 0, "(")
        
        return res







"""
open always <= closed

if open == close, that is valid

"""
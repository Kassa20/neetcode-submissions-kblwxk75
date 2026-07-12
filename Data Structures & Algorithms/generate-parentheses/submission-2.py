class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        op, cl = 0, 0

        def dfs(s, op, cl):
            
            if op > n: 
                return

            if cl > op:
                return 

            if op == n and cl == n:
                res.append(s)

            dfs(s + "(", op + 1, cl)
            dfs(s + ")", op, cl + 1)
        
            return 


        dfs("", 0, 0)

        return res







class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[0][0] = 1

        for r in range(ROWS):
            for c in range(COLS):
                if r - 1 >= 0 and c - 1 >= 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                elif r - 1 >= 0:
                    dp[r][c] = dp[r-1][c]
                elif c - 1 >= 0:
                    dp[r][c] = dp[r][c-1]


        return dp[ROWS-1][COLS-1]



"""

[[0, 0, 0, 0, 0, 0, 0], 
[0, 5, 4, 3, 2, 1, 0], 
[0, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0]]


"""



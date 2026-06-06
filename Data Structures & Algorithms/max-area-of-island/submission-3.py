class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        def dfs(r, c):
            if( r not in range(ROWS) or c not in range(COLS) or
                grid[r][c] == 0 or visited[r][c]):
                return 0
            
            visited[r][c] = True

            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
                
            return 1 + left + right + up + down


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and visited[r][c] == False:
                    res = max(res, dfs(r, c))
        
        return res



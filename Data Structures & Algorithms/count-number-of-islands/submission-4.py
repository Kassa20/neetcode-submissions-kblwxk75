class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1":
                    q.append((r + 1, c))
                    q.append((r, c + 1))
                    q.append((r - 1, c))
                    q.append((r, c - 1))
                    grid[r][c] = "0"
            
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)


        return islands





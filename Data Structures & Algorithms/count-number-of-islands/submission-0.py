class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0;

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                x, y = q.popleft()
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and 
                        (nr, nc) not in visited and 
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visited.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

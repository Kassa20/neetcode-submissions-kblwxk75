class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()

        def bfs(r, c):
            perimeter = 0
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                seen.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr not in range(ROWS) or nc not in range(COLS)
                         or grid[nr][nc] == 0):
                         perimeter += 1
                    elif (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            
            return perimeter
                        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r, c)
        
        return 0





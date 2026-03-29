class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        _max = 0
        def bfs(r, c):
            nonlocal _max
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            land = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and 
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        land += 1
            _max = max(_max, land)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)        
        return _max

        

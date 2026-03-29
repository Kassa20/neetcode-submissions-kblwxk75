class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1


        
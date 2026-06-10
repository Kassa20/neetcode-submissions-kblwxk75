class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        

        dist = 0
        seen = set()
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r not in range(ROWS) or c not in range(COLS) or
                    grid[r][c] == -1 or (r, c) in seen):
                    continue
                
                seen.add((r, c))
                grid[r][c] = min(grid[r][c], dist)
                
                q.append((r, c + 1))
                q.append((r, c - 1))
                q.append((r + 1, c))
                q.append((r - 1, c))

            dist += 1





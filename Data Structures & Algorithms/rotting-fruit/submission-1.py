class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c - 1])
                    q.append([r, c + 1])
                    q.append([r - 1, c])
                    q.append([r + 1, c])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r in range(ROWS) and c in range(COLS) and 
                     grid[r][c] == 1):
                    grid[r][c] = 2
                    q.append([r, c - 1]) # left
                    q.append([r, c + 1]) # Right
                    q.append([r - 1, c]) # up
                    q.append([r + 1, c]) # down
                    fresh -= 1
            time += 1

        
        return time if fresh == 0 else -1




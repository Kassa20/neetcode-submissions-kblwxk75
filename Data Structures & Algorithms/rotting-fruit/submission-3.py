class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        rotten = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        seen = set()
        time = 0
        while q and fresh > 0:
            has_rotted = False
            for i in range(len(q)):
                r, c = q.popleft()
                if(r not in range(ROWS) or c not in range(COLS)
                    or (r, c) in seen or grid[r][c] == 0):
                    continue
                
                seen.add((r, c))
                if grid[r][c] == 1:  
                    fresh -= 1
                    has_rotted = True
                q.append((r, c + 1))
                q.append((r, c - 1))
                q.append((r - 1, c))
                q.append((r + 1, c))
         
            if has_rotted:
                time += 1
        
        if fresh > 0:
            return -1
        

        return time
                










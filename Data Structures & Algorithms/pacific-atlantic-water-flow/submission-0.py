class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
         
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        pacific = atlantic = False

        def dfs(r, c, prev):
            nonlocal pacific, atlantic 

            if r < 0 or c < 0:
                pacific = True
                return        

            if r >= ROWS or c >= COLS:
                atlantic = True
                return
            if visited[r][c]:
                return
            if heights[r][c] > prev:
                return

            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, heights[r][c])
                if pacific and atlantic:
                    break
            visited[r][c] = False


        for r in range(ROWS):
            for c in range(COLS):
                pacific = atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])

        return res








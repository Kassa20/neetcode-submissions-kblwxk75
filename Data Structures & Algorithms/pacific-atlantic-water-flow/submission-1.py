class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, ath = set(), set()

        def dfs(r, c, prev, seen):

            if (r not in range(ROWS) or c not in range(COLS) or
                (r, c) in seen or heights[r][c] < prev):
                return

            seen.add((r, c))
            dfs(r, c - 1, heights[r][c], seen)
            dfs(r, c + 1, heights[r][c], seen)
            dfs(r - 1, c, heights[r][c], seen)
            dfs(r + 1, c, heights[r][c], seen)

            return

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], ath)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], ath)


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in ath:
                    res.append([r, c])

        return res


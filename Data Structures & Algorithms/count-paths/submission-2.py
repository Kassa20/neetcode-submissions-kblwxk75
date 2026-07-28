class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        cache = defaultdict(int)

        def dfs(r, c):
            if r == ROWS or c == COLS:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            if cache[(r, c)]:
                return cache[(r, c)]

            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            cache[(r, c)] = down + right

            return down + right


        return dfs(0, 0)


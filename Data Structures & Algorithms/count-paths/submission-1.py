class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        seen = set()
        paths = 0
        d = defaultdict(int)

        def dfs(row, col):
            if row == ROWS or col == COLS or (row, col) in seen:
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1

            if d[(row, col)]:
                return d[(row, col)]

            seen.add((row, col))
            right = dfs(row, col + 1) # right
            down = dfs(row + 1, col) # down

            seen.remove((row, col))

            d[(row, col)] = right + down

            return right + down


        return dfs(0, 0)





class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r, c):
            if(r not in range(ROWS) or c not in range(COLS)
                or (r, c) in seen or board[r][c] == 'X'):
                return

            if (board[r][c] == 'O'):
                board[r][c] = 'S'

            seen.add((r, c))

            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r + 1, c)

            return


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1):
                    dfs(r, c)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'






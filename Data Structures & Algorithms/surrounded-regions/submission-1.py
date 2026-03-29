class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and (board[r][c] == "O"):
                    board[r][c] = "T"

        def dfs(r, c):
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited or board[r][c] == "X" ):
                return 

            board[r][c] = "T"
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            return 


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"







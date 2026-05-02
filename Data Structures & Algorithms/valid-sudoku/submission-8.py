class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS, COLS = len(board), len(board[0])

        #rows
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        # cols
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # 3 x 3 
        for r in range(0, ROWS-3, 3):
            for c in range(0, COLS-3, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] == ".":
                            continue
                        elif board[r + i][c + j] in seen:
                            return False
                        seen.add(board[r + i][c + j])
        
        return True





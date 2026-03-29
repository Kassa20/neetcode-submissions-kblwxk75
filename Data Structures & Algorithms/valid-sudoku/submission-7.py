class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS, COLS = len(board), len(board[0])

        #rows
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in seen or int(board[r][c]) < 1 
                    or int(board[r][c]) > 9):
                    return False
                seen.add(board[r][c])

        #cols
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in seen or int(board[r][c]) < 1 
                    or int(board[r][c]) > 9):
                    return False
                seen.add(board[r][c])


        row, col = 0, 0
        while row <= ROWS - 3:
            while col <= COLS - 3:
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] == ".":
                            continue
                        if(board[r][c] in seen or int(board[r][c]) < 1 
                            or int(board[r][c]) > 9):
                            return False 
                        seen.add(board[r][c])

                col += 3
            row += 3


        return True










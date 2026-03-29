class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])


        ROWS, COLS = len(board), len(board[0])
        n = 3
        row, col = 0, 0
        while row <= ROWS-3:
            while col <= COLS-3:
                seen = set()
                for r in range(3):
                    for c in range(3):
                        num = board[row+r][col+c]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
                col += 3
            row += 3       

        return True                   

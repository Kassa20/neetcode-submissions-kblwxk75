class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])


        def rows(col, matrix):
            for r in range(ROWS):
                if matrix[r][col] != 0:
                    matrix[r][col] = "z"

        def cols(row, matrix):
            for c in range(COLS):
                if matrix[row][c] != 0:
                    matrix[row][c] = "z"


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows(c, matrix) #rows
                    cols(r, matrix) #cols

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "z":
                    matrix[r][c] = 0

"""

[0,1,2,0]
[3,4,5,2]
[1,3,1,5]

"""

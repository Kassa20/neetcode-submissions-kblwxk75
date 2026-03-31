class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        copy = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                copy[r][c]= matrix[r][c]

        for r in range(ROWS): 
            for c in range(COLS):
                if(matrix[r][c] == 0):
                    #right
                    for nc in range(c, COLS):
                        copy[r][nc] = 0
                    #left
                    for nc in range(c, -1, -1):
                        copy[r][nc] = 0
                    #up
                    for nr in range(r, -1, -1):
                        copy[nr][c] = 0
                    #down
                    for nr in range(r, ROWS):
                        copy[nr][c] = 0
        
        
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c]= copy[r][c]






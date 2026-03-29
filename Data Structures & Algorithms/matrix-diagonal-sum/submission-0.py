class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        ROWS, COLS = len(mat), len(mat[0])
        seen = set()
        cur_row, cur_col = 0, 0
        res = 0

        #right
        while cur_row < ROWS and cur_col < COLS:
            if (cur_row, cur_col) not in seen:
                res += mat[cur_row][cur_col]
                seen.add((cur_row, cur_col))
            
            cur_row += 1
            cur_col += 1

        cur_row = 0
        cur_col = COLS - 1

        #left
        while cur_row < ROWS and cur_col >= 0:
            if (cur_row, cur_col) not in seen:
                res += mat[cur_row][cur_col]
                seen.add((cur_row, cur_col))

            cur_row += 1
            cur_col -= 1


        return res
        


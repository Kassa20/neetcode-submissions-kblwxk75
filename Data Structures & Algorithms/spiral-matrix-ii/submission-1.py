class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ROWS, COLS = n, n
        left, right = 0, COLS - 1
        bottom, top = ROWS - 1, 0
        
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        curr = 1

        while curr <= n*n:
            # left -> right
            for i in range(left, right+1):
                res[top][i] = curr
                curr += 1
            
            top += 1
            
            # up -> down
            for i in range(top, bottom+1):
                res[i][right] = curr
                curr += 1
            
            right -= 1

            # right -> left
            for i in range(right, left - 1, -1):
                res[bottom][i] = curr
                curr += 1
            
            bottom -= 1

            # bottom -> top
            for i in range(bottom, top-1, -1):
                res[i][left] = curr
                curr += 1
            
            left += 1


        return res













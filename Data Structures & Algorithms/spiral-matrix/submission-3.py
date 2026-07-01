class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        top, left = 0, 0
        bottom, right = ROWS-1, COLS-1


        res = []
        while top <= bottom and left <= right:

            # left -> right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            if top > bottom:
                break
  
            # top -> bottom
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if left > right:
                break

            # right -> left
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # bottom -> top
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1


        return res



"""

[7]
[9]  
[6]

"""

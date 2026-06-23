class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        left, right = 0, COLS - 1


        while top < bottom:
            for i in range(right - left):
                curr = matrix[top][left + i]

                # bottom-left -> top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom-right -> bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top->right -> bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # top-left -> top-right
                matrix[top + i][right] = curr
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1

            



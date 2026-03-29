class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        left, top = 0, 0
        right, bottom = len(matrix)-1, len(matrix)-1
        while left < right and top < bottom:
            for i in range(right - left):
                topLeft = matrix[top][left + i]

                #bottom-left -> top->left
                matrix[top][left + i] = matrix[bottom - i][left] 

                #bottom-right -> bottom->left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #top-right -> bottom->right
                matrix[bottom][right - i] = matrix[top + i][right]

                #top-right
                matrix[top + i][right] = topLeft
            
            left += 1
            top += 1
            bottom -= 1
            right -= 1

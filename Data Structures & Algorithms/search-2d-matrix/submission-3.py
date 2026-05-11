class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        def search(row):
            left, right = 0, COLS - 1
            while left <= right: 
                mid = (left + right) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][0] <= target <= matrix[r][COLS-1] and search(r):
                    return True
                else:
                    break
        
        return False


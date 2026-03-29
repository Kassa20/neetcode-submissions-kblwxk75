class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            left, right = 0, COLS-1
            while left <= right:
                mid = left + ((right-left) // 2)
                if matrix[r][mid] < target:
                    left = mid + 1
                elif matrix[r][mid] > target:
                    right = mid - 1
                elif matrix[r][mid] == target:
                    return True
        return False
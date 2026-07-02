class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])

        seen = set()
        start = image[sr][sc]
        def dfs(r, c, color):
            if (r not in range(ROWS) or c not in range(COLS) or
                (r, c) in seen):
                return 

            seen.add((r, c))
            if image[r][c] != start:
                return 
            
            image[r][c] = color
            dfs(r, c - 1, color)
            dfs(r, c + 1, color)
            dfs(r - 1, c, color)
            dfs(r + 1, c, color)

            return 

        dfs(sr, sc, color)

        return image


"""

[1,1,1],
[1,1,0],
[1,0,1]

"""

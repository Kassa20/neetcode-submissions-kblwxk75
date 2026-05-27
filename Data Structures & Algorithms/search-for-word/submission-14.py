class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r not in range(ROWS) or c not in range(COLS):
                return False

            if visited[r][c] or word[i] != board[r][c]:
                return False

            visited[r][c] = True
            for dr, dc in directions:
                if(dfs(r + dr, c + dc, i + 1)):
                    return True
            
            visited[r][c] = False

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
    
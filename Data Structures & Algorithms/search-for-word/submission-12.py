class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, s):
            if r not in range(ROWS) or c not in range(COLS):
                return False

            if visited[r][c]:
                return False

            s += board[r][c]
            if s == word:
                return True

            visited[r][c] = True
            for dr, dc in directions:
                if(dfs(r + dr, c + dc, s)):
                    return True
            
            visited[r][c] = False

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, ""):
                        return True

        return False
    
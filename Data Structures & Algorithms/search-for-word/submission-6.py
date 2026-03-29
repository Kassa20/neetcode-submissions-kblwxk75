class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        check = []  
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):

            if board[r][c] != word[i]:
                return False

            check.append(board[r][c])
            visited[r][c] = True

            if len(check) == len(word):
                return True

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    not visited[nr][nc]):
                     if dfs(nr, nc, i + 1):
                        return True

            visited[r][c] = False
            check.pop()
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
        


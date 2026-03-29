class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        array = []
        visited = set()
        def dfs(r, c, index):
            nonlocal array
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited):
                return False
            if board[r][c] != word[index]:
                return False

            array.append(board[r][c])
            visited.add((r, c))
            if len(array) == len(word):
                return True


            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, index + 1):
                    return True
       
            array.pop()
            visited.remove((r, c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
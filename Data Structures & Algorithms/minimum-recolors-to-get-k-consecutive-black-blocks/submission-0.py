class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        n = len(blocks)
        l = 0
        white = 0
        black = 0
        res = 10000
        for r in range(n):                
            if blocks[r] == "W":
                white += 1
            if blocks[r] == "B":
                black += 1
            if r - l + 1 == k:
                op = abs(k - black)
                res = min(res, op)
                if blocks[l] == "W":
                    white -= 1
                else:
                    black -= 1
                l += 1

        return res









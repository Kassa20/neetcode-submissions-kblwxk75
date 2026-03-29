class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n+1):
            counter = 0
            for j in range(32):
                if (1 << j) & i:
                    counter += 1
            res.append(counter)

        
        return res
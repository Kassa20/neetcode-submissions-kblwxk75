class Solution:
    def countPrimes(self, n: int) -> int:
        
        seive = [False] * n
        count = 0

        for i in range(2, n):
            if not seive[i]:
                count += 1
                for j in range(i * i, n, i):
                    seive[j] = True
            

        return count
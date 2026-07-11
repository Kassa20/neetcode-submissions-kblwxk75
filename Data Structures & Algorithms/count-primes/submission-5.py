class Solution:
    def countPrimes(self, n: int) -> int:
        
        sieve = [False] * n
        count = 0

        for i in range(2, n):
            if sieve[i] == False:
                count += 1
                for j in range(i*i, n, i):
                    sieve[j] = True
        
        return count
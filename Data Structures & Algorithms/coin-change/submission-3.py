class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        
        return dp[amount] if dp[amount] != float('inf') else -1


"""
dp[0] = 0
dp[1] = 1 + min(dp[1-1]) = 1
dp[2] = 1 + min(dp[1]) = 2
dp[3] = 1 + min(dp[2], dp[0]) = 1
dp[4] = 1 + min(dp[3], dp[1], dp[0]) = 1
dp[5] = 1 + min(dp[4], dp[2], dp[1]) = 2
dp[6] = 1 + min(dp[5], dp[3], dp[2]) = 



"""
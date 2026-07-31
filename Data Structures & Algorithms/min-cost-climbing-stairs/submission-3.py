class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # bottom up
        dp = [0] * (len(cost) + 1)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)+1):
            res = min(dp[i-1], dp[i-2])
            if i < len(cost):
                dp[i] = res + cost[i] 
            else:
                dp[i] = res
        
        return dp[-1]

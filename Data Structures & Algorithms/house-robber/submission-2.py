class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[n-1] = nums[-1]
        dp[n-2] = max(nums[-1], nums[-2])

        res = max(dp[0], dp[1])
        for i in range(n-3, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])    

        return dp[0]






"""
f(i) = the maximmum amount of money to rob, 
        where houses are not adjecent 

dp[i] = nums[i] + dp[i-1]
res = max(res, dp[i])

"""



class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = nums[0]
        res = max(nums[0], nums[1])

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[n]


"""
f(i) = the maximmum amount of money to rob, 
        where houses are not adjecent 

f(0) = 0
f(1) = nums[1]
f(2) = max(f(1), f(i))
f(3) = max(f(2), f(i))

dp[i] = max(dp[i-1], nums[i])

nums=[5, 1, 2, 10, 6, 2, 7, 9, 3, 1]

dp[0, 5, 5, 7, 15, 15, 17, 22, 26, 26, 27]



res = 





"""



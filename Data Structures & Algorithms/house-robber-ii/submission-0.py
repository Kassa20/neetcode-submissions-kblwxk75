class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums) 

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n+1)

        #start = 1st
        dp[0] = 0
        dp[1] = nums[0]

        res = 0
        for i in range(1, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            res = max(res, dp[i])
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            res = max(res, dp[i])


        return res


"""     1. 2. 3  4  5

nums = [2, 9, 8, 3, 6]

 dp=[0, 0, 0, 0, 0, 0]

"""
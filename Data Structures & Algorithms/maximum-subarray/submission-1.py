class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        res = nums[0]

        for i in range(len(nums)):
            _sum = nums[i] 
            res = max(_sum, res)
            for j in range(i+1, len(nums)):
                _sum += nums[j]
                res = max(res, _sum)


        return res


"""

2 + (-3)


"""
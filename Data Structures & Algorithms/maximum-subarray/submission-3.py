class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        res = nums[0]
        _sum = nums[0]

        for i in range(1, len(nums)):

            _sum = max(_sum + nums[i], nums[i])
            res = max(res, _sum)
          

        return res


"""
_sum = 0
res = 5
    
    i
[5, 4, -1, 7, 8]



"""




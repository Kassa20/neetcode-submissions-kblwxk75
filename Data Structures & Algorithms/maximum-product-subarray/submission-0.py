class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp, curMin * num, num)
            res = max(res, curMax)
            
        return res
"""
cmax = 2
cmin = -2
res = 6

-1 -2 -3

I)
    cmax = max(1*-1, -1*1, -1) = -1
    cmin = min(1*-1, -1*1, -1) = -1
    res = max(-1, -1) = -1

II) 
    cmax = max(-2*-1, -2*-1, -2) = 2
    cmin = min(-2*-1, -2*-1, -2) = -2
    res = max(-1, 2) = 2

III)
    cmax = max(-3 * 2, -3 * -2, -3)
    cmin = min(-3 * 2, -3 * -2, -3)
    res = max(2, 6) = 6

"""




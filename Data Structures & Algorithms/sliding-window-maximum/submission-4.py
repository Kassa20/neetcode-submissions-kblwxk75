class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        res = []
        for r in range(k-1, len(nums)):
            _max = -20000
            for i in range(l, r+1):
                _max = max(_max, nums[i])

            res.append(_max)
            l += 1
    
        return res
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = 2 ** 31 - 1
        currSum = 0
        left = 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                res = min(res, right - left + 1) 
                currSum -= nums[left]
                left += 1
        

        return res if res != 2 ** 31 - 1 else 0
            

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        res = 0
        left = 0

        [8, 2, 4, 7]

        for right in range(len(nums)):

            smaller = min(nums[left:right+1])
            larger = max(nums[left:right+1])
            diff = abs(larger - smaller)

            while diff > limit and left < right:
                left += 1
                smaller = min(nums[left:right+1])
                larger = max(nums[left:right+1])
                diff = abs(larger - smaller)

            res = max(res, right - left + 1)

        
        return res




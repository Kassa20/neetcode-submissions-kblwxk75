class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        res = []
        seq = 0
        for num in nums:
            if num-1 not in seen:
                i = num
                while i in seen:
                    i += 1
                seq = max(seq, i-num)

        return seq
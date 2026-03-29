class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        res = []
        seq = 0
        for num in nums:
            if num-1 not in seen:
                count = 0
                i = num
                while i in seen:
                    count += 1
                    i += 1
                seq = max(seq, count)

        return seq
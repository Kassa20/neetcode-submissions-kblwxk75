class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        res = []
        seq = 0

        for num in seen:
            if num - 1 not in seen:
                curr = num 
                while curr in seen:
                    curr += 1
                seq = max(seq, curr - num)
        
        return seq
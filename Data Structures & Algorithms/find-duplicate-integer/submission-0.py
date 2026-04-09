class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        c = Counter(nums)

        for n in c:
            if c[n] >= 2:
                return n


        return -1
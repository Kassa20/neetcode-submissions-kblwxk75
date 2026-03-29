class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        n = len(nums)

        for num in nums:
            d[num] += 1
            if d[num] > math.floor(n/2):
                return num
        
        return -1
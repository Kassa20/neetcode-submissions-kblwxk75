class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        nums.sort()
        freq = 1

        for i in range(len(nums) - 1):

            if nums[i] == nums[i+1]:
                freq += 1
            if freq >= 2:
                return nums[i]
            else:
                freq = 1
 

        return -1
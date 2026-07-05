class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = len(nums) - 1
        copy = []

        for i in range(len(nums)):
            if nums[i] == 0:
                copy.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == 1:
                copy.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == 2:
                copy.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = copy[i]


"""

[1, 2, 0, 1, 2]

"""

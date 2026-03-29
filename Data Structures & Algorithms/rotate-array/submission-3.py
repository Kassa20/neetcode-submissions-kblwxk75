class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(k):
            last = nums[len(nums) - 1]
            for index in range(len(nums)-1, 0, -1):
                nums[index] = nums[index-1]
            nums[0] = last
        
        
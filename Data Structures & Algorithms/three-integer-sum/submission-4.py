class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right: 
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add(tuple((nums[i], nums[left], nums[right])))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return [val for val in list(res)]




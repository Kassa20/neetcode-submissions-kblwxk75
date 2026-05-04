class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            # while i >= 1 and nums[i-1] == nums[i]:
            #     continue

            l, r = i + 1, n - 1

            while l < r: 
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else: 
                    r -= 1

        return list(res)


"""

      i   l        r                  
[-4, -1, -1, 0, 1, 2]
  0   1   2  3  4  5

"""
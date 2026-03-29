class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[k] = nums[i]
                seen.add(nums[k])
                k += 1

        return k



#                   k
#  [2, 10, 30, 40, 30, 40]
#                         i
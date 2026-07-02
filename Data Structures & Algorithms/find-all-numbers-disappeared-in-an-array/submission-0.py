class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []
        copy = []
        n = len(nums)

        for i in range(1, n+1): 
            copy.append(i)

        for num in copy:
            if num not in nums:
                res.append(num)



        return res
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * 2 * n
        index = 0

        for num in nums:
            ans[index] = num
            index += 1

        for num in nums:
            ans[index] = num
            index += 1

        return ans
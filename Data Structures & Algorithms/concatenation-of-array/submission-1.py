class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * 2 * n
        p = 0
        p2 = n

        for num in nums:
            ans[p] = num
            ans[p2] = num
            p += 1
            p2 += 1


        return ans
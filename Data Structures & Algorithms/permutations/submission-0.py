class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        for li in permutations(nums):
            res.append(li)

        return [list(li) for li in res]

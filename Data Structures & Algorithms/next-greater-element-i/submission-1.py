class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        next_great = [-1] * 10000
        stack = []
        res = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                next_great[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(nums2[i])

        for query in nums1:
            res.append(next_great[query])



        return res
    

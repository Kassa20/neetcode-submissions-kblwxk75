class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = m
        i = 0
        while i < len(nums2):
            nums1[index] = nums2[i]
            i += 1
            index += 1

        nums1.sort()

    
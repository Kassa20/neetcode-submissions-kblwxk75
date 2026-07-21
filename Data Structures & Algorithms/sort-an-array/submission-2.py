class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(list1, list2):
            index1, index2 = 0, 0
            merged = []

            while index1 < len(list1) and index2 < len(list2):
                if list1[index1] < list2[index2]:
                    merged.append(list1[index1])
                    index1 += 1
                else:
                    merged.append(list2[index2])
                    index2 += 1
            
            while index1 < len(list1):
                merged.append(list1[index1])
                index1 += 1
            
            while index2 < len(list2):
                merged.append(list2[index2])
                index2 += 1
            
            return merged


        def mergesort(nums):
            if len(nums) <= 1:
                return nums

            m = len(nums) // 2

            list1 = mergesort(nums[:m])
            list2 = mergesort(nums[m:])


            return merge(list1, list2)


        return mergesort(nums)



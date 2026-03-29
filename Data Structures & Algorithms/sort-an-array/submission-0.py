class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            left, right = 0, 0
            merged = []                                 
            minLen = min(len(arr1), len(arr2))           
            while left < len(arr1) and right < len(arr2):
                if arr1[left] < arr2[right]:
                    merged.append(arr1[left])
                    left += 1
                else:
                    merged.append(arr2[right])
                    right += 1

            while left < len(arr1):
                merged.append(arr1[left])
                left += 1
            while right < len(arr2):
                merged.append(arr2[right])
                right += 1
            return merged
                                                
                                                
        def mergeSort(nums):
            if len(nums) == 1:                  
                return nums
            left = 0
            right = len(nums)
            mid = (right - left) // 2
            arr1 = mergeSort(nums[:mid])
            arr2 = mergeSort(nums[mid:])
            return merge(arr1, arr2)

        return mergeSort(nums)
        


 
                










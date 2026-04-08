class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r: 
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        if nums[pivot] == target:
            return pivot

        def search(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        res = search(0, pivot) #left
        if res != -1:
            return res
        
        return search(pivot, len(nums) - 1) #right










"""
                
[2, 3, 4, 5, 6, 1]
       
[6, 1, 2, 3, 4, 5]


"""
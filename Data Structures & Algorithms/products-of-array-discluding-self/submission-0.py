class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return []


        arr = [1] * len(nums)
        pre = nums[0]
        for i in range(1, len(nums)):
            arr[i] =  pre
            pre *= nums[i]

        arr2 = [1] * len(nums)
        post = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            arr2[i] = post
            post *= nums[i]

        print(arr)
        print(arr2)

        res = [0] * len(arr)
        for i in range(len(arr)):
            res[i] = arr[i] * arr2[i]

        return res
        
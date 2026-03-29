class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for i in range(len(nums)):
            d[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
    
            for j in range(i+1, len(nums)):
                d[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
    
                num1 = nums[i]
                num2 = nums[j]
                num3 = -1*(num1+num2)
                if d[num3] > 0:
                    res.append([num1, num2, num3])
            
            for j in range(i+1, len(nums)):
                d[nums[j]] += 1

        return res








  
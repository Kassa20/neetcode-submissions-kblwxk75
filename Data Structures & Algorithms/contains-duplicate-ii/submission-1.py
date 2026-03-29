class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]
            if num in seen:
                index = seen[num]
                if abs(index - i) <= k:
                    return True

            seen[num] = i

        return False
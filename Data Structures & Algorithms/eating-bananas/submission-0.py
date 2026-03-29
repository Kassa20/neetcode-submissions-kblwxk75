class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxK = max(piles)
        res = maxK
        
        left, right = 1, maxK
        while left <= right:

            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / mid)
            
            if hours <= h:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
       

        return res
        

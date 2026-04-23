class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        # left
        left_max = [0] * n
        left_max[0] = 0
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i-1])

        right_max = [0] * n
        right_max[n-1] = 0
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        res = 0
        for i in range(n): 
            s = min(left_max[i], right_max[i]) - height[i]
            if s < 0:
                continue
            res += s

        return res


"""
max(l, r) - h[i]



"""
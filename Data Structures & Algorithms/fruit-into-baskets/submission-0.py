class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        d = defaultdict(int)
        n = len(fruits)
        res = 0
        left = 0
        for right in range(n):
            fruit = fruits[right]
            d[fruit] += 1
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            
            res = max(res, right - left + 1)


        return res

# 2: 2
# 3: 1
#              r
# [1, 2, 3, 2, 2]
#     l

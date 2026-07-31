class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # top-down
        d = defaultdict(int)
        def dfs(i):
            if i == 0:
                d[i] = cost[i]
                return d[i]
            if i == 1:
                d[i] = cost[i]
                return d[i]
            if d[i]:
                return d[i]

            if i < len(cost):
                res = min(dfs(i-1), dfs(i-2)) + cost[i]
                d[i] = res
            else:
                res = min(dfs(i-1), dfs(i-2))

            return res

        val = dfs(len(cost))
        print(d)

        return val

"""




"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = set()
        subset = []
     
        def dfs(i, total):
            if total == target:
                res.add(tuple(subset.copy()))
                return 
            if i >= len(candidates) or total > target:
                return 
            
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            subset.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return [list(subset) for subset in res]





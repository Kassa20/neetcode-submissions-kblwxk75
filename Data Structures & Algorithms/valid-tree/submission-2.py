class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        d = defaultdict(list)
        seen = set()

        for edge in edges:
            start, end = edge[0], edge[1]
            d[start].append(end)
            d[end].append(start)

        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for child in d[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
 
            return True

        return dfs(0, -1) and len(seen) == n


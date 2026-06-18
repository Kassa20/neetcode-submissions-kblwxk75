class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > (n - 1):
            return False

        d = defaultdict(list)
        seen = set()

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            d[node1].append(node2)
            d[node2].append(node1)

        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
            for n in d[node]:
                if n == prev: continue
                if not dfs(n, node):
                    return False

            return True

        
        dfs(0, -1)

        return len(seen) == n


# 0: [1, 2, 3]
# 1: [4]



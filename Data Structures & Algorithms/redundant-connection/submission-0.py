class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        def dfs(node, p):
            if node in seen:
                return True

            seen.add(node)
            for child in d[node]:
                if child == p:
                    continue

                if dfs(child, node):
                    return True

            return False


        d = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            d[u].append(v)
            d[v].append(u)
            seen = set()
        
            if dfs(u, -1):
                return [u, v]



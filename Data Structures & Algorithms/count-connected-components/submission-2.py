class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            d[node1].append(node2)
            d[node2].append(node1)


        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            for n in d[node]:
                dfs(n)

            return


        seen = set()
        res = 0
        for node in range(n):
            if node not in seen:
                res += 1
                dfs(node)

        return res



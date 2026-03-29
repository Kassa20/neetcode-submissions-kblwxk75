class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d = defaultdict(list)
        seen = set()

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            d[node1].append(node2)
            d[node2].append(node1)

        def dfs(node):
            if node in seen:
                return 

            seen.add(node)
            for n in d[node]:
                dfs(n)
            
            return 
        
        comp = 0
        while len(seen) < n:
            for node in range(n):
                if node not in seen:
                    comp += 1
                    dfs(node)
        
        return comp


"""
2 - 3 - 1
"""

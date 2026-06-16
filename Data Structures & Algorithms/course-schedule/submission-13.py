class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = defaultdict(list)
        for course1, course2 in prerequisites:
            d[course1].append(course2)
        
        
        seen = set()
        def dfs(node):
            if node in seen:
                return False
            if d[node] == []:
                return True

            seen.add(node)
            for n in d[node]:
                if not dfs(n):
                    return False
            seen.remove(node)
            d[node] = []

            return True
            
        for n in range(numCourses):
            if not dfs(n):
                return False

        return True







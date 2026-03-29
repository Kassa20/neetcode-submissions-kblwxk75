class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = defaultdict(list)
        visited = set()
        visiting = set()

        for pre in prerequisites:
            course, req = pre
            d[course].append(req)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False

            visited.add(course)
            visiting.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True










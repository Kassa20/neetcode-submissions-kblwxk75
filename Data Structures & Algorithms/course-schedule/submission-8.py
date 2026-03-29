class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        courses = defaultdict(list)
        for p in prerequisites:
            courses[p[0]].append(p[1])

        seen = set()
        def dfs(course):
            if course not in courses:
                return True
            if course in seen:
                return False
            
            seen.add(course)
            for preq in courses[course]:
                if not dfs(preq):
                    return False
            
            seen.remove(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True






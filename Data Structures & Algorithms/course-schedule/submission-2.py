class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        d = defaultdict(list) 

        for prereq in prerequisites:
            course, pre = prereq[0], prereq[1]
            d[course].append(pre)
        visited = set()

        def dfs(course):
            if not d[course]:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            d[course] = []
            return True            

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True






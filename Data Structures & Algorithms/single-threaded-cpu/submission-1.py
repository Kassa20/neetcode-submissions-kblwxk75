class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key=lambda t: t[0])

        min_heap, time = [], tasks[0][0]
        res, i = [], 0

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not min_heap:
                time = tasks[i][0]
            else:
                proTime, index = heapq.heappop(min_heap)
                time += proTime 
                res.append(index)

        return res





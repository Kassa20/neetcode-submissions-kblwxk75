class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt((x**2 + y**2))
            heapq.heappush(max_heap, (-dist, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        for val in max_heap:
            dist, x, y = val
            res.append([x, y])

        return res

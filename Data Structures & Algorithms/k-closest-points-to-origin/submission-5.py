class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []

        for point in points: #O(nlogn)
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (dist, [x, y]))
        
        while len(res) < k: #O(klogn)
            d , point = heapq.heappop(minHeap)
            res.append(point)
        
        return res



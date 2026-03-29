class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []

        for point in points: #O(nlogk)
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (-1 * dist, [x, y]))
            if len(minHeap) > k: 
                heapq.heappop(minHeap)
        
        while minHeap: #O(klogk)
            d, point = heapq.heappop(minHeap)
            res.append(point)

        
        return res



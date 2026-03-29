
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []

        for corr in points:
            x = corr[0]
            y = corr[1]
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (-d, [x, y]))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        for i in range(len(minHeap)):
            res.append(heapq.heappop(minHeap)[1])

        return res






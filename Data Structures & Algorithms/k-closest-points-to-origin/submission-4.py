
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []

        for corr in points:
            x = corr[0]
            y = corr[1]
            d = math.sqrt(x**2 + y**2)
            minHeap.append((d, [x, y]))
     
        heapq.heapify(minHeap)

        while k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1

        return res






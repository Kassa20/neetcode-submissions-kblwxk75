class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        m = defaultdict(list)
        distances = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            d = math.sqrt(x**2 + y**2)
            distances.append([d, x, y])

        heapq.heapify(distances)
        while k > 0:
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1

        return res






class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        m = defaultdict(list)
        distances = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            d = math.sqrt(x**2 + y**2)
            distances.append(d)

        distances = [-s for s in distances]
        for i in range(len(points)):
            m[-1 * distances[i]].append((points[i][0], points[i][1]))

        
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)

        
        for i in range(len(distances)):
            dis = -1 * heapq.heappop(distances)
            coord = m[dis]

            for j in range(len(coord)):
                if(len(res)) == k:
                    break
                x, y = coord[j][0], coord[j][1]
                res.append([x, y])

        return res






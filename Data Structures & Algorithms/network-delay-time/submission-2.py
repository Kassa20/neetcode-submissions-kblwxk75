class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        d = defaultdict(list)

        for time in times:
            node1, node2, time = time[0], time[1], time[2]
            d[node1].append([node2, time])
        
        seen = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap: 
            w1, node = heapq.heappop(minHeap)
            if node in seen:
                continue

            res = max(res, w1)
            seen.add(node)

            for nei, w2 in d[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (w1 + w2, nei))


        return res if len(seen) == n else -1


"""

"""



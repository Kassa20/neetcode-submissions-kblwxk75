class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        max_heap = []
        for c in count:
            freq = count[c]
            max_heap.append(-freq)

        heapq.heapify(max_heap)
        
        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        d = defaultdict(int)
        for task in tasks:
            d[task] += 1

        max_heap = []
        for t in d:
            freq = d[t]
            max_heap.append(-freq)

        heapq.heapify(max_heap)        
        q = deque()
        time = 0
        
        while q or max_heap:
            time += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                freq, _ = q.popleft()
                heapq.heappush(max_heap, freq)

        return time




"""
1. Most fequent tasks need to be completed first. Why?
    - Each task has a cooldown before we complete
    a similar task. Most frequent task will have he most
    cooldowns. Hence, in those cooldowns, we can pull 
    other tasks to be more efficient. The alternative 
    would be to complete the most freq tasks in the end
    when we wont have other tasks to do while we are idle.

2. A queue, hashmap and a heap are needed. Why use a queue?
    - Each task will have an order to which it needs
    completion. By using a queue, the front of the queue
    will always maintain the true task next in line. 
    A heap will help since we need to constantly get the 
    most frequent task. Finally, a hashmap is needed to 
    count the freq of each task. 
"""
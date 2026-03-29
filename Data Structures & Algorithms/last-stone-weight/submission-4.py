class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minHeap = [-1 * num for num in stones] 
        heapq.heapify(minHeap) #O(n)

        while len(minHeap) > 1:
            x = -1 * heapq.heappop(minHeap)
            y = -1 * heapq.heappop(minHeap)
            
            if x == y:
                continue
            heapq.heappush(minHeap, -1 * abs(x-y))
        
        
        return 0 if not minHeap else abs(minHeap[0])
        

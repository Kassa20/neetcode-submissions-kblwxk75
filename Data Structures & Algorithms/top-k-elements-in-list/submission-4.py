class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        d = defaultdict(int)
        minHeap = []
        res = []

        for num in nums: #O(n)
            d[num] += 1
        
        for key in d: #O(n)
            minHeap.append((-d[key], key))

        heapq.heapify(minHeap) #O(n)

        while len(res) < k and minHeap: #O(klogm)
            freq, val = heapq.heappop(minHeap)
            res.append(val)


        return res
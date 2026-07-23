class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        minHeap = []
        res = []

        for num in arr:
            diff = abs(num - x)
            minHeap.append((diff, num))
        
        heapq.heapify(minHeap)

        for i in range(k):
            _, num = heapq.heappop(minHeap)
            res.append(num)
        
        res.sort()
        
        return res



        
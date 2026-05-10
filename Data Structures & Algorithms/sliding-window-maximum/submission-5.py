class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] < i - (k - 1):
                    heapq.heappop(heap)

                res.append(-heap[0][0])

        return res


"""
max_heap = 3, (2)

[2, 1, 3] 0, 1, 1
2, [1, 3, 0], 1, 1
2, 1, [3, 0, 1], 1
2, 1, 3, [0, 1, 1]  i = 5


"""
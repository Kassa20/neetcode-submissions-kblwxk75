class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        mheap = []
        for n in nums:
            mheap.append(n)
        heapq.heapify(mheap)

        i = len(nums) - k
        for j in range(i): 
            heapq.heappop(mheap)


        return mheap[0]


# [2, 3, 1, 5, 4], k = 2, i = 3

# [1, 2, 3]








'''
we have to continually get the 
largest element = heap
'''
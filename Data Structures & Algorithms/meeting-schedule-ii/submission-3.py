"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x : x.start)
        min_heap = []

        for interval in intervals: 

            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
        

        return len(min_heap)



"""
key = 0

0: (1, 5)
1: (2, 6)
2: (3, 7)
3: (4, 8)
4: (5, 9)


 1   5
   2   6
     3   7
       4    8
          5    9


"""






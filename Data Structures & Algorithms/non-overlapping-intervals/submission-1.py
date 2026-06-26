class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        n = len(intervals)

        curr = intervals[0]
        res = 0
        for i in range(1, n):

            if intervals[i][0] < curr[1]:
                intervals[i][1] = min(intervals[i][1], curr[1])
                res += 1
            
            curr = intervals[i]


        return res

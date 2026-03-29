#compare 2nd value of 1st array 
# 1st value of second array
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        current = intervals[0]
        res = []
        res.append(current)

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
            

        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(reverse=True)
        res = [intervals[0]]
        start = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[1] > start[0]:
                continue
            else:
                res.append(interval)
                start = interval

        return len(intervals) - len(res)
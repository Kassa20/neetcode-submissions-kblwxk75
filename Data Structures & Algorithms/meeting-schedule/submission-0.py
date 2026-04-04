"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        data = sorted(intervals, key=lambda x: (x.start, x.end))
        
        for i in range(len(data)-1):
            first = data[i]
            second = data[i+1]
            if first.end > second.start:
                return False

        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda p: (p.start))
        runningStart = intervals[0].start
        runningEnd = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # Starts in the interval we have already, bad
            if interval.start >= runningStart and interval.start < runningEnd:
                return False
            runningStart = min(runningStart, interval.start)
            runningEnd = max(runningEnd, interval.end)
        return True
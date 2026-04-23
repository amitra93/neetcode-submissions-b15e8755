"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        ctr = 0
        maxCtr = 0
        start = end = 0
        while start < len(intervals):
            if starts[start] < ends[end]:
                ctr += 1
                start += 1
            else:
                ctr -= 1
                end += 1
            maxCtr = max(maxCtr, ctr)
        return maxCtr

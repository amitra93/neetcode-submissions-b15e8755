class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
                continue
            else:
                newIntervalMin = min(interval[0], newInterval[0])
                newIntervalMax = max(interval[1], newInterval[1])
                newInterval = [newIntervalMin, newIntervalMax]
        res.append(newInterval)
        return res
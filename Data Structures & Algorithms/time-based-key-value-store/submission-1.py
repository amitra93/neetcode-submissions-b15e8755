from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        valueList = self.data[key]
        lo = 0
        hi = len(valueList) - 1
        toRet = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # if valueList[mid][0] == timestamp:
            #     return valueList[mid][1]
            if valueList[mid][0] <= timestamp:
                toRet = valueList[mid][1]
                lo = mid+1
            else:
                hi = mid-1
        return toRet

            

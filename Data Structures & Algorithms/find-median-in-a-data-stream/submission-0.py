import heapq

class MedianFinder:

    def __init__(self):
        self.bottomHalf = [] # maxheap
        self.topHalf = [] # minheap

    def addNum(self, num: int) -> None:
        if len(self.bottomHalf) == 0 and len(self.topHalf) == 0:
            heapq.heappush(self.topHalf, num)
            return

        if len(self.bottomHalf) >= len(self.topHalf):
            heapq.heappush(self.topHalf, num)
        else:
            heapq.heappush_max(self.bottomHalf, num)
        
        maxFromBottomHalf = self.bottomHalf[0]
        minFromTopHalf = self.topHalf[0]
        if maxFromBottomHalf <= minFromTopHalf:
            return
        
        # If not, we need to rebalance
        heapq.heappop(self.topHalf)
        heapq.heappop_max(self.bottomHalf)
        heapq.heappush(self.topHalf, maxFromBottomHalf)
        heapq.heappush_max(self.bottomHalf, minFromTopHalf)


    def findMedian(self) -> float:
        print(f"bottom half {self.bottomHalf}, top half {self.topHalf}")

        if len(self.bottomHalf) > len(self.topHalf):
            return self.bottomHalf[0]
        if len(self.bottomHalf) < len(self.topHalf):
            return self.topHalf[0]
        return (self.topHalf[0] + self.bottomHalf[0])/2
        
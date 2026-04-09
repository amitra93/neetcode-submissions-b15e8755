import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = list([-i for i in nums])
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -1*val)
        kSmallest = heapq.nsmallest(self.k, [i for i in self.heap])
        return -1 * kSmallest[-1]

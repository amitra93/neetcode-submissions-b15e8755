class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        else:
            kthLargest = self.heap[0]
            if val <= kthLargest:
                return self.heap[0]
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        for i in range(len(nums) - k):
            print(f"popping {heapq.heappop(nums)}")
        return heapq.heappop(nums)
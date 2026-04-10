import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        maxLcsLength = 1
        currentLcsLength = 1
        lastVal = float('inf')
        while len(nums) > 0:
            val = heapq.heappop(nums)
            print(val)
            if val == lastVal:
                continue
            if val - lastVal == 1:
                currentLcsLength += 1
            else:
                currentLcsLength = 1
            if currentLcsLength > maxLcsLength:
                maxLcsLength = currentLcsLength
            lastVal = val
        return maxLcsLength
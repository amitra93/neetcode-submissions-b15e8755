class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTotal = float('-inf')
        runningTotal = 0
        for i in nums:
            runningTotal = max(i, runningTotal + i)
            maxTotal = max(maxTotal, runningTotal)
            print(f"runningTotal {runningTotal}, maxTotal {maxTotal}")
        return maxTotal
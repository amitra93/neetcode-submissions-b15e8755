class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights) - 1
        maxWaterSoFar = 0
        while lo < hi:
            water = min(heights[lo], heights[hi]) * (hi - lo)
            if water > maxWaterSoFar:
                maxWaterSoFar = water
            if heights[lo] > heights[hi]:
                hi -= 1
            elif heights[lo] < heights[hi]:
                lo += 1
            else:
                lo += 1
        return maxWaterSoFar
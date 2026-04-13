class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            hoursNeeded = sum([math.ceil(i/mid) for i in piles])
            if hoursNeeded > h:
                lo = mid + 1
            else:
                hi = mid
        return lo
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[lo] < nums[mid]:
                lo = mid
            elif nums[lo] > nums[mid]:
                hi = mid
        raise ValueError

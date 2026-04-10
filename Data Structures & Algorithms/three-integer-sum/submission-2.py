class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        toRet = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sum = nums[lo] + nums[hi] + nums[i]
                if sum == 0:
                    toRet.append([nums[lo], nums[hi], nums[i]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif sum > 0:
                    hi -= 1
                elif sum < 0:
                    lo += 1
        return toRet

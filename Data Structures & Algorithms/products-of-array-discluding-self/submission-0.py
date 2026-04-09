class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeroes = 0
        runningProduct = 1
        for i in nums:
            if i == 0:
                numZeroes += 1
            else:
                runningProduct *= i
            if numZeroes > 1:
                return [0] * len(nums)
        toRet = []
        for i in nums:
            if numZeroes == 0:
                toRet.append(int(runningProduct/i))
            elif i != 0:
                toRet.append(0)
            elif i == 0:
                toRet.append(int(runningProduct))
        return toRet

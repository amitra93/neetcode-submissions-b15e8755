class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        toRet = 0
        for i in nums:
            toRet ^= i
        return toRet
class Solution:
    def hammingWeight(self, n: int) -> int:
        toRet = 0
        while n > 0:
            toRet += n % 2
            n = n//2
        return toRet
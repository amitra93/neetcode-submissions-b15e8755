class Solution:
    def reverseBits(self, n: int) -> int:
        retVal = 0
        for i in range(32):
            digit = n%2
            retVal = retVal * 2 + digit
            n = n//2
        return retVal
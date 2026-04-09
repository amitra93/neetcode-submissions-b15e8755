class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = 0
        while True:
            num = self.getSquares(n)
            if num in seen:
                return False
            if num == 1:
                return True
            seen.add(num)
            n = num
        raise ValueError
        
    def getSquares(self, n: int) -> int:
        return sum(int(i)**2 for i in str(n))
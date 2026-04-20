class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expandFromCenter(l: int, r: int) -> int:
            localCount = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                localCount += 1
                l -= 1
                r += 1
            return localCount
            
        for i in range(0, len(s)):
            count += expandFromCenter(i, i)
            count += expandFromCenter(i, i+1)
        return count

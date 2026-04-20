class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def maxOdd(i: int) -> str:
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        def maxEven(i: int) -> str:
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        maxPalindrome = ""
        for i in range(0, len(s)):
            odd = maxOdd(i)
            even = maxEven(i)
            # print(f"at {i}, maxOdd is {odd} and maxEven is {even}")
            if len(odd) > len(maxPalindrome):
                maxPalindrome = odd
            if len(even) > len(maxPalindrome):
                maxPalindrome = even
        return maxPalindrome

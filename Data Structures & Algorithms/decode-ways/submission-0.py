import collections

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if int(s[i-1: i+1]) in range(10, 27):
                dp[i+1] += dp[i-1]
        print(dp)
        return dp[-1]
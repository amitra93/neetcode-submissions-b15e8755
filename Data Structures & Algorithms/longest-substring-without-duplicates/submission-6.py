class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        unique = set()
        longest = 0
        start = 0
        for c in s:
            if c not in unique:
                unique.add(c)
            else:
                while c in unique:
                    unique.remove(s[start])
                    start += 1
                unique.add(c)
            longest = max(longest, len(unique))
        return longest

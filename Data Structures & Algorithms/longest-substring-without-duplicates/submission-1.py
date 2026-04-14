class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        uniqueSet = set()
        uniqueSet.add(s[0])
        maxUnique = 1
        start = 0
        end = 1
        while end < len(s):
            print(uniqueSet)
            if s[end] not in uniqueSet:
                uniqueSet.add(s[end])
                end = end + 1
                maxUnique = max(maxUnique, (end - start))
            else:
                while s[end] in uniqueSet:
                    uniqueSet.remove(s[start])
                    start = start + 1
        return maxUnique
            
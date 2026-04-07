class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency1 = dict()
        frequency2 = dict()
        for i in s:
            frequency1[i] = frequency1.get(i, 0) + 1
        for i in t:
            frequency2[i] = frequency2.get(i, 0) + 1
        return frequency1 == frequency2
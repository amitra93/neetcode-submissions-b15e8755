from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        for st in strs:
            sortedSt = "".join(sorted(st))
            freqMap[sortedSt].append(st)
        return list(freqMap.values())
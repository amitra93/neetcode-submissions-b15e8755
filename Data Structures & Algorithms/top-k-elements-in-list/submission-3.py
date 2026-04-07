from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freqSorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        freqSortedList = list(freqSorted.keys())
        toRet = []
        for i in range(k):
            toRet.append(freqSortedList[i])
        return toRet
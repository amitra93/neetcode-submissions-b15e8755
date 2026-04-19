class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def dictify(s: str) -> dict:
            sdict = {}
            for i in s:
                sdict[i] = sdict.get(i, 0) + 1
            return sdict

        ctr = len(s1)
        expected = dictify(s1)
        actual = dictify(s2[0: ctr])
        while ctr < len(s2):
            if expected == actual:
                return True
            actual[s2[ctr - len(s1)]] -= 1
            if actual[s2[ctr - len(s1)]] == 0:
                del actual[s2[ctr - len(s1)]]
            actual[s2[ctr]] = actual.get(s2[ctr], 0) + 1
            ctr += 1
        return expected == actual

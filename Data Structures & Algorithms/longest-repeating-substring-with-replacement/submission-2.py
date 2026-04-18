class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {s[0]: 1}
        maxLength = 1
        startIdx = 0

        def lengthOfStringExceptMostFrequent():
            lengthOfAll = sum(frequencies.values())
            lengthOfMostFrequent = 0
            for i in frequencies:
                lengthOfMostFrequent = max(lengthOfMostFrequent, frequencies[i])
            return lengthOfAll - lengthOfMostFrequent

        for i in range(1, len(s)):
            frequencies[s[i]] = frequencies.get(s[i], 0) + 1
            while lengthOfStringExceptMostFrequent() > k:
                frequencies[s[startIdx]] -= 1
                startIdx += 1
            maxLength = max(maxLength, sum(frequencies.values()))
        return maxLength
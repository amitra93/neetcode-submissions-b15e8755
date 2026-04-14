class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pos = [False] * (len(nums) + 1)
        for i in nums:
            pos[i] = True
        for i in range(len(pos)):
            if not pos[i]:
                return i
        raise KeyError
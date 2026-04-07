class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        containsSet = {}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in containsSet:
                return sorted([index, containsSet[complement]])
            containsSet[val] = index
        raise KeyError
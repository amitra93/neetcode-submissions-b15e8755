class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def houseRob1(numsSubset: List[int]) -> int:
            maxRob = [0] * len(numsSubset)
            maxRob[0] = numsSubset[0]
            print(f"numsSubset = {numsSubset}")
            print(f"maxRob = {maxRob}")
            maxRob[1] = max(numsSubset[1], maxRob[0])
            for i in range(2, len(numsSubset)):
                maxRob[i] = max(numsSubset[i] + maxRob[i-2], maxRob[i-1])
            return maxRob[-1]

        return max(houseRob1(nums[0: -1]), houseRob1(nums[1:]))
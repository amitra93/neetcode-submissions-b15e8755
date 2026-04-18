class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0 = 0
        rob1 = 0
        for i in nums:
            temp = max(i + rob0, rob1)
            rob0 = rob1
            rob1 = temp
        return rob1
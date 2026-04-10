class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            currentSum = numbers[lo] + numbers[hi]
            if currentSum == target:
                return [lo+1, hi+1]
            elif currentSum < target:
                lo += 1
            elif currentSum > target:
                hi -= 1
        return []
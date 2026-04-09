class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(str(d) for d in digits))
        number += 1
        string = str(number)
        return [int(d) for d in string]
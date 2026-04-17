class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        idx = 0
        while idx < n:
            nextArrValue = sum(arr)
            arr[0] = arr[1]
            arr[1] = nextArrValue
            idx += 1
        return arr[0]
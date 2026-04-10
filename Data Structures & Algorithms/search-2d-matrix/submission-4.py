class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowNumLo = 0
        rowNumHi = len(matrix) - 1
        cols = len(matrix[0])
        while rowNumLo <= rowNumHi:
            if matrix[rowNumLo][0] <= target <= matrix[rowNumLo][cols-1]:
                return self.binarySearch(matrix[rowNumLo], target)
            if matrix[rowNumHi][0] <= target <= matrix[rowNumHi][cols-1]:
                return self.binarySearch(matrix[rowNumHi], target)
            rowNumMid = rowNumLo + (rowNumHi - rowNumLo)//2
            if matrix[rowNumMid][0] <= target <= matrix[rowNumMid][cols-1]:
                return self.binarySearch(matrix[rowNumMid], target)
            if target < matrix[rowNumMid][0]:
                rowNumHi = rowNumMid-1
            else:
                rowNumLo = rowNumMid+1
        return False
    
    def binarySearch(self, rows: List[int], target: int) -> bool:
        lo = 0
        hi = len(rows)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if target == rows[mid]:
                return True
            if target > rows[mid]:
                lo = mid+1
            else:
                hi = mid-1
        return False
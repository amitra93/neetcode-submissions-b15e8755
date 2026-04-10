from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        rowsets = defaultdict(set)
        colsets = defaultdict(set)
        subboxsets = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rowsets[i]:
                    return False
                if val in colsets[j]:
                    return False
                if val in subboxsets[(i//3, j//3)]:
                    return False
                rowsets[i].add(val)
                colsets[j].add(val)
                subboxsets[(i//3, j//3)].add(val)
        return True

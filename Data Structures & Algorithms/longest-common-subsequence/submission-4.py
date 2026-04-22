class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            # print(text1[i])
            for j in range(n):
                # print(text2[j])
                if text1[i] == text2[j]:
                    matrix[i+1][j+1] = 1 + matrix[i][j]
                else:
                    matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])
                # print(matrix)
        return matrix[-1][-1]
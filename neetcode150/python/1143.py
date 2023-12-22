"""1143"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1) + 1, len(text2) + 1
        table = [[0 for _ in range(n)] for _ in range(m)]

        for i in reversed(range(0, m - 1)):
            for j in reversed(range(0, n - 1)):
                if text1[i] == text2[j]:
                    table[i][j] = 1 + table[i + 1][j + 1]
                else:
                    table[i][j] = max(table[i + 1][j], table[i][j + 1])

        return table[0][0]
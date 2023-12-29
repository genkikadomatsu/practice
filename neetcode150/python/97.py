"""97"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
                
        table = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(len(table)):
            for j in range(len(table[0])):
                
                if i == 0 and j == 0:
                    table[i][j] = True

                if i != 0 and s1[i - 1] == s3[i + j - 1] and table[i - 1][j]:
                    table[i][j] = True

                if j != 0 and s2[j - 1] == s3[i + j - 1] and table[i][j - 1]:
                    table[i][j] = True

        return table[-1][-1]
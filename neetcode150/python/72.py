"""72"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1) + 1, len(word2) + 1
        table = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    table[i][j] = 0
                elif i == 0:
                    table[i][j] = j
                elif j == 0:
                    table[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(
                        table[i - 1][j],
                        table[i][j - 1],
                        table[i - 1][j - 1]
                    )
                
        return table[-1][-1]
"""518"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        table = [0 for _ in range(amount + 1)]
        table[0] = 1

        for coin in coins:
            for i in range(len(table)):
                if i - coin >= 0:
                    table[i] += table[i - coin]
        
        return table[-1]
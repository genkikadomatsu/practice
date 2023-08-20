"""LeetCode 17: Letter Combinations of a Phone Number

Given a series of numbers, return the possible strings the numbers could
represent.
1:       2: abc   3: def
4: ghi   5: jkl   6: mno
7: pqrs  8: tuv   9: wxyz
"""


# LeetCode 17
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        """Return all possible lettter combinations.""" 

        if not digits:
            return []
        
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        def backtrack(current: str, i: int) -> None:
            
            if i == len(digits):
                result.append(current)
                return

            for c in digit_to_char[digits[i]]:
                backtrack(current + c, i + 1)
            
        backtrack("", 0)
        return result

print(Solution().letterCombinations("23"))



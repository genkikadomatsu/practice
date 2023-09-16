# LeetCode 131
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Return all possibe palindromic partitions."""

        result = []

        def palindromic(s: str) -> bool:
            """
            Returns True if s is a palindrome.
            
            Note: For this problem, empty strings aren't considered palindromes.
            """

            if s == "":
                return False
         
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False

            return True

        def backtrack(current: List[str], part: str, i: int) -> None:
            
            # Base case: End of s, make partition if valid, else return.
            if i == len(s):
                if palindromic(part):
                    result.append(current + [part])
                return
            
            # Recursive case: Make a partition (if valid).
            if palindromic(part):
                backtrack(current + [part], s[i], i + 1)

            # Recursive case: Don't make a partition.
            backtrack(current, part + s[i], i + 1)

        backtrack([], "", 0)
        return result
           
"""70 Climbing Stairs"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Return the number of distinct ways one can climb n stairs when they
        are able to ascend either 1 or 2 stairs per step.
        """

        a = 1
        b = 1

        if n <= 1:
            return a

        for i in range(2, n + 1):
            a, b = b, a + b
        
        return b
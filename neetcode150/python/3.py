# LeetCode 3
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Return the length of the longest possible substring in s that has no
        repeating characters.
        """

        l, r = 0, 0
        char_to_count = defaultdict(int)
        maxln = 0

        while r < len(s):
            char_to_count[s[r]] += 1
            
            while char_to_count[s[r]] > 1:
                char_to_count[s[l]] -= 1
                l += 1
            
            maxlen = max(0)
"""LeetCode 5"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the length of the longest substring."""

        longest_length = 0
        longest_start = 0
        longest_end = 0

        # Check length for odd palindromes
        for i in range(len(s)):
            l, r = i - 1, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_length:
                    longest_start = l
                    longest_end = r
                    longest_length = r - l + 1
                r += 1
                l -= 1
            
        # Check length for even palindromes
        for i in range(len(s)):
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_length:
                    longest_start = l
                    longest_end = r
                    longest_length = r - l + 1
                r += 1
                l -= 1

        return s[longest_start:longest_end + 1]

print(Solution().longestPalindrome("babad"))

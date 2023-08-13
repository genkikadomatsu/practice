"""LeetCode 424: Longest Repeating Character Recplacement

Given some string s, you can replace k characters. Given all potential
replacements of k characters in the string, return the length of the longest
mono-character substring.

"AABABBA", 1 => 4
"ABAB", 2 => 4
"AAB", 0 => 2
"""

class Solution:
 
    def characterReplacement(self, s: str, k: int) -> int:
        """
        This is the optimal O(n) approach, where we track the most frequent
        character in the 'window', becaues that character will be the one that
        has the longest mono-character substring.

        :param s: The input string.
        :param k: The maximum number of character replacements allowed.
        :returns: The length of the longest repeated-character string possible.
        """
        char_counts = {}
        result, start_i = 0, 0
        
        for end_i in range(len(s)):
            # Update the count of the current character.
            char_counts[s[end_i]] = 1 + char_counts.get(s[end_i], 0)

            # Shift the start until our window is only using k replacements. 
            while (end_i - start_i + 1 - max(char_counts.values())) > k: # O(26) 
                char_counts[s[start_i]] -= 1
                start_i += 1

            result = max(result, end_i - start_i + 1)
    
        return result

    def naive_approach(self, s: str, k: int) -> int:
        """
        This is the naive approach, which is still O(n), but not optimal.

        :param s: The input string.
        :param k: The maximum number of character replacements allowed.
        :returns: The length of the longest repeated-character string possible.
        """

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        max_length = 0

        for c in alphabet: 
            replacements, start_i = 0, 0

            for end_i in range(len(s)):

                # Case: Non-matching char.
                if s[end_i] != c:

                    # Sub-case: A replacement is available.
                    if replacements < k:
                        replacements += 1

                    # Sub-case: Non-matching char, and replacements unavailable.
                    else:
                        # Shift start pointer 'over' 1 non-matching char.
                        while s[start_i] == c:
                            start_i += 1
                        start_i += 1

                # We do +1 here because the string is pointer inclusive.                
                max_length = max(end_i - start_i + 1, max_length)

        return max_length 
    
print(Solution().characterReplacement(input("s:"), int(input("k:"))))
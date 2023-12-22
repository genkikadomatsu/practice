"""LeetCode 91"""

class Solution:
    def numDecodings(self, s: str) -> int:

        num_ways = [0 for _ in range(len(s) + 1)]
        num_ways[-1] = 1 # Empty string

        for i in reversed(range(len(s))):
            
            if s[i] == "0":
                
                # In this case the string is invalid
                if i - 1 < 0 or s[i - 1] not in ["1", "2"]:
                    return 0
                
                # Note that num_ways[i] is already 0 here 
                continue
            
            # This isn't a 0 so we can consider it a valid single digit
            num_ways[i] += num_ways[i + 1]

            # We might also be able to consider it a valid double digit 
            if (
                i + 1 in range(len(s)) and # If we are in range and
                int(s[i]) * 10 + int(s[i + 1]) in range(1, 27) # Is alpha
            ):
                num_ways[i] += num_ways[i + 2]

        return num_ways[0]

"""LeetCode 139"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i_to_end_is_breakable = [False for _ in range(len(s) + 1)]
        i_to_end_is_breakable[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                # Condition for s[i:] to be breakable 
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    if not i_to_end_is_breakable[i]:
                        i_to_end_is_breakable[i] = i_to_end_is_breakable[i + len(w)]
    
        return i_to_end_is_breakable[0]

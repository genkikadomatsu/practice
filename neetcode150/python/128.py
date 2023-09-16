#128.py Longest Consecutive Sequence
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
				

        smol = min(nums)
        big = max(nums)

        nums = list(set(nums))
        slots = [[] for x in range(big - smol)]
        print("len", len(slots))
 
        for n in nums:
            print(n, n - smol)
            slots[n - smol - 1] = n

        maxlen, currlen = 0, 0
        consecutive = True
        for s in slots:
            if s:
                currlen += 1
            else:
                maxlen = max(currlen, maxlen)

        return maxlen

s = Solution()

print(s.longestConsecutive([100,4,200,1,3,2]))

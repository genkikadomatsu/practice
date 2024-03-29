from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        tortoise, hare = 0, 0 # the list's length is >= 2

        while tortoise != hare or tortoise == 0:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
        
        anchor = 0

        while anchor != tortoise:
            anchor, tortoise = nums[anchor], nums[tortoise]
        
        return tortoise

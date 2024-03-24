from typing import List

# LeetCode 153
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Returns the minimum element in the list.
        
        The list is assumed to be in sorted ascending order, but potentially
        rotated to the right any number of times.
        """
        
        l, r = 0, len(nums) - 1

        while True:
            
            i = (l + r) // 2

            if nums[i] <= nums[i - 1]:
                return nums[i]

            if nums[i] < nums[r]:
                r = i - 1
            else:
                l = i + 1
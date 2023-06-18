from typing import List

# LeetCode 153
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Returns the minimum element in the list.
        
        The list is assumed to be in sorted ascending order, but potentially
        rotated to the right any number of times.
        """

        left, right = 0, len(nums) - 1
        result = float("inf")

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1

        return min(result, nums[left]) # this could also be nums[right]            

while True:
    print(Solution().findMin([int(x) for x in input("list:").split()]))
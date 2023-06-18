from typing import List


# LeetCode 33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Given a list, returns the index of the target.
        
        The list is sorted in acending order but potentially rotated. Returns -1
        if the target is not in the list.
        """


        left, right = 0, len(nums) - 1

        while left < right:
            
            mid = (left + right) // 2
            print(nums[left], nums[mid], nums[right])
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        if nums[right] == target:
            return right

        return - 1
while True:
    print(Solution().search([int(n) for n in input("list:").split()], int(input("target:"))))


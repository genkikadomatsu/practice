from typing import List

# LeetCode 287
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        tortoise, hare = nums[0], nums[nums[0]] 

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        
        new_tortoise = 0
       
        while tortoise != new_tortoise:
            tortoise = nums[tortoise]
            new_tortoise = nums[new_tortoise] 
        
        return tortoise

while True:
    print(Solution().findDuplicate([int(n) for n in input("list:").split()]))
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print("sorted:", nums)
        result = []

        for i in range(len(nums) - 2):
            
            # If the current element is a duplicate of the previous, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If this elemen is positive, 0 sum isn't possible
            if nums[i] > 0:
                break


            a = i
            b = a + 1
            c = len(nums) - 1

            while b < c:
                if nums[a] + nums[b] + nums[c] <  0:
                    b += 1
                elif nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1

                    while nums[b] == nums[b - 1] and b < c:
                        b += 1

                    # This is unecessary but more explicit, debatable...
                    while nums[c] == nums[c + 1] and b < c:
                        c -= 1
                    
        return result



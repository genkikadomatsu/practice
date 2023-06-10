from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        end_k = len(nums) - k

        def quickSelect(l, r):
            
            swap = l
            for i in range(l, r):

                if nums[i] <= nums[r]:
                    nums[swap], nums[i] = nums[i], nums[swap]
                    swap += 1

            nums[swap], nums[r] = nums[r], nums[swap]

            if swap > end_k:
                return quickSelect(l, swap - 1)
            elif swap < end_k:
                return quickSelect(swap + 1, r)
            else:
                return nums[swap]

        return quickSelect(0, len(nums) - 1)

s = Solution()
print(s.findKthLargest([1,2,3,4,5], 3))            
                

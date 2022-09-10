class Solution:
    def search(self, nums: list[int], target: int) -> int:


        front, back = 0, len(nums)
        

        while back != front:
            i = int((front + back) / 2) 
            print(front, back, i)
            if target == nums[i]:
                return i

            elif target < nums[i]:
                back = i 

            elif target > nums[i]:
                front = i + 1


        return -1

sol = Solution()


i1 = [1, 2]
i2 = [1, 2, 3, 4, 5]
i3 = [1, 3, 4, 6, 7, 9]
i4 = [-1, 0, 3, 5, 9, 12]
i5 = [0]

print(sol.search(i4 , 9))

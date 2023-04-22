class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort() #nlogn
        result = []

        for i in range(len(nums) - 2):

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
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
                    

        
        return result


input1 = [-1,0,1,2,-1,-4]
input2 = [0,1,1]
input3 = [0,0,0]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ docstring """
        
        
        d = {}

        # step 1: foreach index, add the value as a key in the dictionary and the index as a value in a list
        for i in range(len(nums)):
            try:
                d[nums[i]].append(i)
            except BaseException: 
                d[nums[i]] = [i]
        
        # step 2: for each value, find the corresponding required value to sum and check if it exists
        for key, value in d.items():
            if (target - key) in d:
                for firstIndex in value:
                    for secondIndex in d[target-key]:
                        if firstIndex != secondIndex:
                            return [firstIndex, secondIndex]



print("Two Sum")

# test inputs
input1 = ([1,2,3], 4) # basic
input2 = ([1,2,3,1], 4) # basic
input3 = ([0,0,0,1,4], 4) # basic
input4 = ([-1, 2, 3, 4, 5], 3) # negatives

# failed submission inputs
failedInput = ([3,2,4], 6) # duplicate indexes are not allowed
failedInput1 = ([2,5,5,11], 10) # wrong method of testing dictionary membership ANKI THIS

# checking solution
solution = Solution()
def checkSol(input):
    print("INPUT")
    print(input)
    print("OUTPUT")
    print(solution.twoSum(*input))

# check solutions
checkSol(input1)
checkSol(input2)
checkSol(input3)
checkSol(input4)
checkSol(failedInput)
checkSol(failedInput1)
# LeetCode 338
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        offset = 1
        result = [0]
        i = 0

        for i in range(n):
            if i == offset:
                offset = offset * 2
            result.append(1 + result[i + 1 - offset])
                
        return result

# i = 0
# result = [0]
# offset = 1
# appends 1 + result[0 + 1 - 1] = 1

# i = 1
# result = [0 , 1]
# offset = 1
# appends 1 + result[1 + 1 - 1] = 1
# offset and i are 1 so offset is now 2

# i = 2
# result  = [0, 1, 1]
# offset = 2
# appends 1 + result[2 + 1 - 2] = 2
# i == offset so offset is now 4

# i = 3
# result = [0, 1, 1, 2]
# offset = 2
# appends 1 + result[3 + 1 - 4] = 1

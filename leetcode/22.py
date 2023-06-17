from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        curr_str = ""

        def add_parenthesis(open, closed):

            nonlocal curr_str

            if open < n:
                curr_str = curr_str + "("
                add_parenthesis(open + 1, closed)
                curr_str = curr_str[:-1]

            if closed < open:
                curr_str = curr_str + ")"
                add_parenthesis(open, closed + 1)
                curr_str = curr_str[:-1]

            if open == closed == n:
                result.append(curr_str)

        add_parenthesis(0, 0)
        return result    


while True:
    print(Solution().generateParenthesis(int(input("n:"))))
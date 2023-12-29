"""678"""
class Solution:
    def checkValidString(self, s: str) -> bool:

        pseudo_stack_min = 0
        pseudo_stack_max = 0

        for c in s:
            
            if c == "(":
                pseudo_stack_min += 1
                pseudo_stack_max += 1

            elif c == ")": 
                pseudo_stack_min -= 1
                pseudo_stack_max -= 1

                if pseudo_stack_max < 0:
                    return False
            
            elif c == "*":
                pseudo_stack_min -= 1
                pseudo_stack_max += 1

            pseudo_stack_min = max(0, pseudo_stack_min)

        return pseudo_stack_min == 0 

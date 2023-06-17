# LeetCode 853
from typing import List, Tuple
PARAMS = (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])

class Solution:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Returns the number of resulting car fleets."""

        i_s_p = [(i, s, position[i]) for i, s in enumerate(speed)]
        i_s_p.sort(key=lambda elem: elem[2])
        position_speed_stack = [(elem[2], elem[1]) for elem in i_s_p]

        print(position_speed_stack, target)
        num_fleets = 0

        while position_speed_stack:
            
            print(position_speed_stack, "------", num_fleets)
            head = position_speed_stack.pop()

            if not position_speed_stack:
                print("only one left")
                return num_fleets + 1

            tail = position_speed_stack.pop()

            if self.is_fleet(tail, head, target):
                position_speed_stack.append(head)
            else:
                position_speed_stack.append(tail)
                num_fleets += 1

        return num_fleets        


    def is_fleet(self,
                 tail: Tuple[int, int],
                 head: Tuple[int, int], 
                 target: int
    )-> bool:
        """Determines if tail can reach head before head reaches distance."""

        head_position, head_speed = head
        tail_position, tail_speed = tail

        head_time = (target - head_position) / head_speed
        tail_time = (target - tail_position) / tail_speed
        
        return head_time >= tail_time

print(Solution().carFleet(*PARAMS))
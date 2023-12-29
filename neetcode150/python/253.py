"""253"""
from typing import List
from collections import deque

class Interval:
    def __init__(self, start,end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]" 

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> bool:

        start_times = deque(sorted([i.start for i in intervals]))
        end_times = deque(sorted([i.end for i in intervals]))
        max_num_rooms = 0
        current_num_rooms = 0

        current_start, current_end = start_times.popleft(), end_times.popleft()
        if len(intervals) == 1:
            return 1

        while start_times or end_times:        

            while current_start < current_end:
                current_num_rooms += 1
                max_num_rooms = max(max_num_rooms, current_num_rooms)

                if start_times:
                    current_start = start_times.popleft() 
                else:
                    return max_num_rooms

            
            current_end = end_times.popleft()
            current_num_rooms -= 1

        return max_num_rooms

assert 1 == Solution().min_meeting_rooms([Interval(2, 7)])
assert 2 == Solution().min_meeting_rooms([Interval(0,30),Interval(5,10),Interval(15,20)])
assert 1 == Solution().min_meeting_rooms([Interval(1,3), Interval(3,4)])
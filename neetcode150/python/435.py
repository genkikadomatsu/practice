"""435"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda l: l[0])
        is_overlapping = lambda a, b: a[0] <= b[0] < a[1] or b[0] < a[1] <= b[1]
        previous_interval = intervals[0]
        min_removed = 0

        for interval in intervals[1:]:

            if is_overlapping(previous_interval, interval):
                previous_interval = interval if interval[1] < previous_interval[1] else previous_interval
                min_removed += 1
                continue
            
            previous_interval = interval

        return min_removed

print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
from typing import List
import heapq
from collections import deque

# LeetCode 621
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_counts = {}
        
        for c in tasks:
            task_counts[c] = task_counts.get(c, 0) + 1

        task_counts = [-count for count in list(task_counts.values())]
        heapq.heapify(task_counts)
        result = 0
        q = deque([])

        # Event loop effectively on each time unit
        while task_counts or q:

            
            # If no ready items, jump time to next item in q
            if task_counts: 
                just_popped = heapq.heappop(task_counts)
                just_popped += 1
 
                if n and just_popped:
                    q.append((just_popped, n))
                elif just_popped:
                    heapq.heappush(task_counts, just_popped)

            # Tick the cooldowns and take out if it is done
            if q:
                if not q[0][1]:
                    heapq.heappush(task_counts, q.popleft()[0])

                q = deque([(elem[0], elem[1] - 1) for elem in q])

            result += 1
        
        return result

s = Solution()
cin = "Hello world"

while cin != "q":
    cin = input("list: ")
    print(s.leastInterval(cin.split(" "), 2))    
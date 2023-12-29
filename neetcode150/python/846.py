"""846"""
from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = {}

        for n in hand:
            count[n] = count.get(n, 0) + 1
        
        pq = [k for k in count.keys()]
        heapq.heapify(pq)

        while pq:
            current_value = pq[0]

            for _ in range(groupSize):
                
                count[current_value] = count.get(current_value, 0) - 1

                if count[current_value] < 0:
                    return False
                
                elif count[current_value] == 0:
                    val = heapq.heappop(pq)
                    
                    if val != current_value:
                        return False

                current_value += 1

        return True

print(Solution().isNStraightHand([1,2,3,4,5,6], 2))
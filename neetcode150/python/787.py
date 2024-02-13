"""787"""
from typing import List
from math import inf
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        costs = [0 if node == src else inf for node in range(n)]

        for _ in range(k + 1):
            frozen_costs = costs.copy()

            for source, destination, cost in flights:
                new_cost = frozen_costs[source] + cost

                if new_cost < frozen_costs[destination] and new_cost < costs[destination]:
                    costs[destination] = frozen_costs[source] + cost
 
        return costs[dst] if costs[dst] != inf else -1

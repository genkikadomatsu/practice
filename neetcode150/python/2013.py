"""2013"""
from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point 
        
        for x, y in self.points:
            if abs(px - x) == abs(py - y) != 0:
                if (px, y) in self.points and (x, py) in self.points:
                    count += (
                        self.points[(px, y)] *
                        self.points[(x, py)] *
                        self.points[(x, y)]
                    )
                    
        return count            

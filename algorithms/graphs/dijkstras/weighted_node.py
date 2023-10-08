"""Implements a basic weighted node for a graph."""
from typing import List

class WeightedNode:
    """A graph node/vertex."""

    def __init__(self, id: int, neighbors: List["Node"] = None):
        """Set this node's ID and neighbors."""

        self.id = id
        self.visited = False
        if not neighbors:
            self.neighbors = [] # [(neighbor, distance_to_neighbor)]
        else:
            self.neighbors = neighbors
    
    def add_outgoing_edge(self, node: "Node", distance: int) -> None:
        """Make an edge from this node to another."""

        self.neighbors.append((node, distance))

    def __repr__(self) -> str:
        return "WeightedNode" + str(self.id)

    def __lt__(self, other):
        return self.id < other.id

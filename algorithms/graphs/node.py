"""Implements the most basic node for a graph."""
from typing import List, Optional

class Node:
    """A graph node/vertex."""

    def __init__(self, id: int, neighbors: List["Node"] = None):
        """Set this node's ID and neighbors."""

        self.id = id
        self.visited = False
        if not neighbors:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    
    def add_outgoing_edge(self, node: "Node") -> None:
        """Make an edge from this node to another."""
        self.neighbors.append(node)

    def __repr__(self) -> str:
        return str(self.id)

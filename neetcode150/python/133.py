"""133 Clone Graph

Given a node in an UNDIRECTED connected graph, return a deep copy of the graph.
"""

from typing import Optional

class Node:
    """Defines a node, which is our input."""

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Return a deep copy of a graph given a reference to a Node.

        Args:
            node (Node): A node in a connected graph.
        Returns:
            Node: The copy of the original node (in the deep copy graph).
        """

        if not node:
            return None

        new_root = Node(node.val)  
        dfs_stack = [node]
        original_to_copies = {node: new_root}

        while dfs_stack:
            current = dfs_stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in original_to_copies:
                    new_copy = Node(neighbor.val)
                    original_to_copies[neighbor] = new_copy
                    original_to_copies[current].neighbors.append(new_copy)
                    dfs_stack.append(neighbor)
                else:
                    # Copy already exists
                    original_to_copies[current].neighbors.append(original_to_copies[neighbor]) 

        return new_root

            

 

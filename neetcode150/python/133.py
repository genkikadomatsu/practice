"""133 Clone Graph

Given a node in an UNDIRECTED connected graph, return a deep copy of the graph.

In this python context, a deep copy is equivalent by value rather than identity.
A deep copy is it's own distinct object in memory.
"""

from typing import Optional

class Node:
    """Defines a node, which is our input."""

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """There are several viable optimal solutions for this."""

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """Return a deep copy of a grpah given a reference to a Node.

        Perform DFS on the graph while making copies of the original.

        Args:
            node (Node): A node in a connected graph.
        Returns:
            Node: The copy of the original node (in the deep copy graph). 
        """

        if not node:
            return None

        dfs_stack = [node]
        new_root = Node(node.val)
        old_to_new = {node: new_root}

        while dfs_stack:
            current_node = dfs_stack.pop()
            
            for neighbor in current_node.neighbors:
               
                if neighbor not in old_to_new:
                    dfs_stack.append(neighbor)
                    old_to_new[neighbor] = Node(neighbor.value)

                old_to_new[current_node].neighbors.append(old_to_new[neighbor])

        return new_root
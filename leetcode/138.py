from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current_node = head
        nodes = []

        # Copy nodes into a list
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next

        # Assign source_index of the random pointed to node 
        for i, n in enumerate(nodes):
            if n.random:
                if hasattr(n.random, "source_index"):
                    n.random.source_index.append(i)
                else:
                    n.random.source_index = [i]

        # Initialize a new empty list of nodes
        new_nodes = [Node(n.val, None, None) for n in nodes]

        # Set the next and random attributes 
        for i, n in enumerate(new_nodes):

            # Set next
            if i < len(nodes) - 1: 
                n.next = new_nodes[i + 1]

            # Set random
            if hasattr(nodes[i], "source_index"):
                for si in nodes[i].source_index:
                    new_nodes[si].random = n

        return new_nodes[0] 
            
"""
Sample implementation of Tarjan's algorithm, which finds strongly connected
components in a graph.
"""
from node import Node
from example_graphs import graph1, graph2

def tarjans(graph: list[Node]):
    """Yields strongly connected components of a graph."""
    
    tarjan_stack = []
    time = 0    
    strongly_connected_components = []

    def dfs(node: Node):

        # Initialize Node for Tarjan's 
        nonlocal time
        time += 1
        node.exploration_time = time
        node.low_link = node.exploration_time
        node.visited = True
        tarjan_stack.append(node)

        # Explore this node's unvisited neighbors.
        for neighbor in node.neighbors:
            if not neighbor.visited:
                dfs(neighbor)
        
        # Set low link to the min of (still stacked) neighbors' low links. 
        for neighbor in node.neighbors:
            if neighbor in tarjan_stack:
                node.low_link = min(node.low_link, neighbor.low_link)

        # Check if this node starts a SCC.
        if node.low_link == node.exploration_time:
            last_popped = None
            scc = []

            # If so, pop from stack until this node is popped. All the popped
            # nodes combined are one SCC.
            while last_popped != node:
                last_popped = tarjan_stack.pop()
                scc.append(last_popped)

            strongly_connected_components.append(scc)

    for node in graph:
        if not node.visited:
            dfs(node)

    yield from strongly_connected_components

# Pick some unvisited node to perform our procedure on.
for scc in tarjans(graph2()):
    print(scc)

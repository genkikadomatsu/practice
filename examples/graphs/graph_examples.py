"""Some example graphs represented as adjacency lists."""
from node import Node



def graph1():
    """Has three strongly connected components.
    
    See ./tarjans_graph.png for visual.
    """
    
    n0, n1, n2, n3, n4 = Node(0), Node(1), Node(2), Node(3), Node(4)
    n5, n6, n7 = Node(5), Node(6), Node(7)
    n0.add_outgoing_edge(n1)
    n1.add_outgoing_edge(n2)
    n2.add_outgoing_edge(n0)
    n3.add_outgoing_edge(n7)
    n3.add_outgoing_edge(n4)
    n4.add_outgoing_edge(n5)
    n5.add_outgoing_edge(n0)
    n5.add_outgoing_edge(n6)
    n6.add_outgoing_edge(n0)
    n6.add_outgoing_edge(n2)
    n6.add_outgoing_edge(n4)
    n7.add_outgoing_edge(n3)
    n7.add_outgoing_edge(n5)
   
    return [n0, n1, n2, n3, n4, n5, n6, n7]


def graph2():
    """Graph 1 but with different ordering of edges in adjacency lists."""

    n0, n1, n2, n3, n4 = Node(0), Node(1), Node(2), Node(3), Node(4)
    n5, n6, n7 = Node(5), Node(6), Node(7)
    n7.add_outgoing_edge(n3)
    n3.add_outgoing_edge(n7)
    n6.add_outgoing_edge(n2)
    n6.add_outgoing_edge(n4)
    n0.add_outgoing_edge(n1)
    n1.add_outgoing_edge(n2)
    n2.add_outgoing_edge(n0)
    n3.add_outgoing_edge(n4)
    n4.add_outgoing_edge(n5)
    n5.add_outgoing_edge(n0)
    n5.add_outgoing_edge(n6)
    n6.add_outgoing_edge(n0)
    n7.add_outgoing_edge(n5)
   
    return [n4, n5, n6, n7, n0, n1, n2, n3]

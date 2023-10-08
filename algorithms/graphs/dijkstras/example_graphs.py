from weighted_node import WeightedNode

node_0 = WeightedNode(0)
node_1 = WeightedNode(1)
node_2 = WeightedNode(2)
node_3 = WeightedNode(3)
node_4 = WeightedNode(4)

node_0.add_outgoing_edge(node_1, 4)
node_0.add_outgoing_edge(node_2, 1)

node_1.add_outgoing_edge(node_3, 1)

node_2.add_outgoing_edge(node_3, 5)
node_2.add_outgoing_edge(node_1, 2)

node_3.add_outgoing_edge(node_4, 3)


graph_1 =[
    node_0,
    node_1,
    node_2,
    node_3,
    node_4
]
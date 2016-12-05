# Ignore for now, using the one in graph.py

import nodes
import uber
import passengers

node1 = Node(0, [], [], 0, 0, 1)
node2 = Node(1, [], [], 2, 0, 1)
node3 = Node(2, [], [], 1, 3, 1)
node4 = Node(3, [], [], 4, 4, 1)
node5 = Node(4, [], [], 5, 2, 1)
node6 = Node(5, [], [], 7, 4, 1)
node7 = Node(6, [], [], 8, 7, 1)
node8 = Node(7, [], [], 4, 7, 1)
node9 = Node(8, [], [], 2, 6, 1)
node10 = Node(9, [], [], 0, 8, 1)

Node.add_neighbor(node1, node2)
Node.add_neighbor(node1, node3)
Node.add_neighbor(node2, node3)
Node.add_neighbor(node3, node4)
Node.add_neighbor(node4, node5)
Node.add_neighbor(node5, node6)
Node.add_neighbor(node6, node7)
Node.add_neighbor(node3, node9)
Node.add_neighbor(node9, node8)
Node.add_neighbor(node9, node10)
Node.add_neighbor(node4, node8)


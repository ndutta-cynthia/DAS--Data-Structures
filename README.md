# Heap-Data-Structure-
HEAP- Is a complete binary tree data structure that satisfies the heap proprietary.

BINARY TREE- A binary tree is a kind of tree data structure where each node can have a maximum of two children,(nodes) referred to as the left and right children.

  USES.
1. Heaps are often used to implement priorities queues when the smallest/largest element is is the root of the tree.
2. Used when one needs to access the max/min value quickly.

PROPERTIES.

1. Ordering- Nodes must be arranged in an order according to values which follow the max/min heap property.

Min Heap - the values of each node/child is greater/equal to its parent.(value (parent) <= value(child)). 

Max Heap- values of each child/node is less than its parent.(value(parent) >=value (value(child) ))

2. Structural- It is structured to have 4 levels/ it should be a complete binary tree.

All levels of a heap should be full except the last one
Nodes must be filled from left to write strictly.

HEAP OPERATIONS.

1. INSERTION- This is done from top to bottom and left- right.
In max heap -Insert the value then keep swapping if the node is greater than parent node.
In min heap - insert then keep swapping if the value is less the parent value.

2. DELETE- One deletes the root node, move the last node to the parent node and bubble.
Min heap - Delete the smallest value, move the last node to the parent node and bubble down
Max heap - Delete the biggest value,move the last node to the parent node and bubble down

heappush − Adds an element to the heap without changing the heap that is already there.

heappop − The function yields the heap's lowest data element.
# DAS--Data-Structures

**A queue **is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed. Think of it like a line of people waiting for service: the person who arrives first is served first.
Key Characteristics of Queues

FIFO Order: The order of processing is strictly maintained.

Dynamic Size: Queues can grow and shrink as elements are added or removed.

Linear Structure: Elements are organized in a sequential manner.

**OPERAIONS**
Enqueue: Add an element to the rear of the queue.

Dequeue: Remove and return the element from the front of the queue.

Peek/Front: Return the element at the front without removing it.

IsEmpty: Check if the queue is empty.

Size: Return the number of elements in the queue.

**TYPES**

Simple Queue: The basic FIFO queue.

Circular Queue: The last position is connected back to the first position to make the queue circular, optimizing space usage.

Priority Queue: Elements are removed based on priority rather than order of arrival. Higher priority elements are dequeued before lower priority ones.

Double-Ended Queue (Deque): Allows insertion and deletion of elements from both the front and the rear.

**APPLICATIONS**

Task Scheduling: Managing tasks in operating systems and CPU scheduling.

Breadth-First Search (BFS): Used in graph algorithms to explore nodes level by level.

Print Queue: Managing print jobs in printers.

Buffer Management: In data streams, such as video or audio processing.

Asynchronous Data Transfer: In networking, where data packets are queued for processing.

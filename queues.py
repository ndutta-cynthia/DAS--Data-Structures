class Node:
    """A node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """A simple queue implementation using a linked list."""
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        new_node = Node(item)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  
            self.rear = new_node        
        self.size += 1               

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        removed_node = self.front   
        self.front = self.front.next    
        if self.front is None:         
            self.rear = None            
        self.size -= 1                 
        return removed_node.data

    def peek(self):
        """Return the element at the front without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data        
    def get_size(self):
        """Return the number of elements in the queue."""
        return self.size


if __name__ == "__main__":
    queue = Queue()
    

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
 
    print("Front item:", queue.peek()) 
    
    
    print("Dequeued item:", queue.dequeue())  
    print("Front item after dequeue:", queue.peek())  
    
 
    print("Queue size:", queue.get_size())  
    
    
    queue.dequeue()
    queue.dequeue()
    

    print("Is the queue empty?", queue.is_empty()) 
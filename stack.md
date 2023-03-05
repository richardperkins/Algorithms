# Stack

**Stacks** Follow the LIFO (Last In, First Out) model. Stacks are also easy to implement and efficient. Use **Push** and **Pop** methods to add to and remove from the stack.

## Example
```py
class Stack:
    def __init__(self):
        self.list = []
        pass
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()
```

# Queue

**Queues** follow the FIFO (first-in, first-out) order. Queues are perfect for managing jobs and tasks. Queues are trickier to implement and should be used when order of objects retrieved matters. Use **Enqueue** and **Dequeue** methods in place of Push and Pop.

## Example

```py
class Queue:
    def __init__(self):
        self.list = []
        pass
    def enqueue(self, item):
        self.list.insert(0,item)
    def dequeue(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return None
```
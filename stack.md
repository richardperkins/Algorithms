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


# Dictionary
**Dictionaries** use named index pointers to assign and retrieve data. 

| Dictionary operation | Unsorted Array | Sorted Array |
|----------------------|----------------|--------------|
| $$Search(L, k)$$ | $$O(n)$$ | $$O(log n)$$ |
| $$Insert(L, x)$$ | $$O(1)$$ | $$O(n)$$ |
| $$Delete(L, x)$$ | $$O(1)$$ | $$O(n)$$ |
| $$Successor(L, x)$$ | $$O(n)$$ | $$O(1)$$ |
| $$Predecessor(L, x)$$ | $$O(n)$$ | $$O(1)$$ |
| $$Minimum(L)$$ | $$O(n)$$ | $$O(1)$$ |
| $$Maximum(L)$$ | $$O(n)$$ | $$O(1)$$ |


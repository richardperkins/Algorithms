# Binary Search Trees   

Binary search trees requires fast access to *two elements*. **Rooted binary trees** are recursively defined as either being (1) empty or (2) a root node with two rooted binary trees. 

## Implementation

### Python
```py
class Tree:
    def __init__(item, parent=None, left=None, right=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right
```

### C#
```cs
struct Tree {
    itemType item;
    BinarySearch *parent;
    BinarySearch *left;
    BinarySearch *right;
};
```

## Binary Search Algorithm

Starting from the root node, if the value for $x$ is less than the node's value, search the left node. Otherwise, search using the right node. 

### C#
```cs
Tree *SearchTree(Tree *l, item_type item) {
    if (l == null)
        return null;
    
    if (item == l.item)
        return l;
    
    if (item < l.item)
        return SearchTree(l.left, item);
    else
        return SearchTree(l.right, item);
}
```

## Finding Minimum and Maximum Elements in a Tree

### Efficiency

$$O(n)$$

### Example
#### C#

```cs
Tree *FindMinimum(Tree *t) {
    Tree *min;      // Pointer to minimum

    if (t == null)
        return null;
    
    min = t;
    while (min.left != NULL) {
        min = min.left;
    }

    return min;
}
```

## Traversal in a Tree

Visiting all nodes within a tree is crucial in many algorithms. Listing all node labels in a tree is a prime example application of traversal.

### Efficiency

$$O(n)$$

### C#

```cs
void TraverseTree(Tree *l) {
    if (l != null) {
        TraverseTree(l.left);
        # Insert processing method here
        TraverseTree(l.right);
    }
}
```

## Insertion

### Efficiency

$$O(h)$$

### C#

```cs
void InsertTree(Tree *l, ItemType x, Tree *parent) {
    Tree *p = new Tree();

    if (l == null) {
        p.item = x;
        p.parent = parent;
        p.left = null;
        p.right = null;
        *l = p;
        return;
    }

    if (x < (*l).item)
        InsertTree(&((*l)).left, x, *l);
    else
        InsertTree(&((*l)).right, x, *l);
}
```

## Deletion

Deleting a node from a tree is more tricky than inserting a new one. How do we handle the deletion of a node from the tree? Does the entire branch disappear or does it reattach to the deleted node's parent?

The example below assumes the branch reattaches to the deleted node's parent.

### Efficiency

$$O(h)$$

### C#
```cs
void DeleteTree(Tree l) {
    if (l.left != null)
        l.left.parent = l.parent;
    if (l.right != null)
        l.right.parent = l.parent;
    
    remove(l);
}
```





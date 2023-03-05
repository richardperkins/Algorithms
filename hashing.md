# Hashing

**Hashing** is a mathematical method to convert characters into integers. A practical example of this is the [Dictionary](dictionary.md).

## Issues

### Hash Size
Converting data into an integer is problematic. The hashing function converts a string to an integer hash.

$$H(S) =
\sum_{i=0}^{|S|−1}
\alpha^{|S|−(i+1)} × char(s_i)$$

The result easily becomes too large for computers to handle. The number of hash table slots quickly fill up (denoted by $m$). Limiting slots to $0-m$ resolves the issue.

### Collision
However, by limiting hash table slots, a new problem is created: **Collision**. Collisions happen when two different values hash to the same value. 

To do this
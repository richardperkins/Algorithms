# Insertion sort

Time complexity: O(N<sup>2</sup>)

Space: O(1)

[insertion-sort.py]

```py
"""
    Sort an array using insertion sort algorithm
"""
def insertion_sort(myArray):
    # Iterate each digit
    for i in range(1,len(myArray)):
        j = i

        # Work backwards until current digit is in place
        while j > 0 and (myArray[j] < myArray[j-1]):
            # Swap current digit and previous digit
            myArray[j-1], myArray[j] = myArray[j], myArray[j-1]
            j -= 1
    return myArray
```
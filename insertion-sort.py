"""
    Sort using insertion sort algorithm
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


print("Using insertion sort")

# Initialize array
myArray = [10,4,50,2,100,495,6,4]
print("Array before: ", myArray)

# Sort array
myArray = insertion_sort(myArray)
print("Array after: ", myArray)


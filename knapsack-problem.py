"""
    The knapsack problem.

    We are given N items where each item has some weight and profit associated with it. We are also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. The target is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 

    Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].
"""

def knapsack(capacity, itemWeights, itemValues, n):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # n'ths item cannot exceed capacity
    if itemWeights[n-1] > capacity:
        return knapsack(capacity, itemWeights, itemValues, n-1)
    # Return maximum between item included and not included
    else:
        return max(
            itemValues[n-1] + knapsack(capacity - itemWeights[n-1], itemWeights, itemValues, n-1),
            knapsack(capacity, itemWeights, itemValues, n-1)
        )

def knapsack2(t, s, r, n):
    if n == 0:
        return r

    if s[n-1] + r > t:
        return knapsack2(t, s, r, n-1)
    else:
        return knapsack2(t, s, s[n-1] + r, n-1)



# Driver code
capacity = 100
itemWeights = [30,20,50,10]
itemValues = [10,50,30,100]
n = len(itemWeights)

result = knapsack(capacity, itemWeights, itemValues, n)
result2 = knapsack2(22, [1,2,5,9,10], 0, 5)
print(result)
print(result2)


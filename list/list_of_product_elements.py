
"""Problem Statement #

Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
Input: #

A list of numbers (could be floating points or integers)
Output: #

A list such that each index has a product of all the numbers in the list except the number stored at that index.
Sample Input #

arr = [1,2,3,4]

Sample Output #

arr = [24,12,8,6]"""

def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


print(find_product([1, 2, 3, 4]))


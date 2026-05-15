#create a linear search and binary search algorithm using array
# create an arry
import numpy as np
a = np.array([1, 2, 3, 4, 5,8,6])
# Search for an element in the array using linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found
# Search for an element in the array using binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target element
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if the target element is not found

# Test the functions
target = 5
print("Array:", a)
print("Searching for:", target)
print("Linear search result (index):", linear_search(a, target))
print("Binary search result (index):", binary_search(a, target))

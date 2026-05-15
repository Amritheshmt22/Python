# create an arry
import numpy as np
a = np.array([1, 2, 3, 4, 5])

# Search for an element in the array
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found

# Example usage
target = 3
result = search(a, target)
if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
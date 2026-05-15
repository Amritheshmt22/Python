# Binary Serach using array

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 8]
    target = 2
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")
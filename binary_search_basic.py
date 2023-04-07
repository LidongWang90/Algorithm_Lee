def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


'''
arr is the sorted array to be searched and target is the element to be searched for. 
The function returns the index of the target element in the arr array, or -1 if the element is not found.

The algorithm works by repeatedly dividing the search interval in half, 
until the target element is found or the interval is empty. At each step, 
the middle element of the interval is compared to the target element, 
and the search interval is narrowed down to the left or right half of the array, 
depending on whether the middle element is less than or greater than the target element.
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # with the first item in the arr which is 0
    start = 0
    # the end is last value in the arr
    end = len(arr)-1
    # while loop through the arr
    while start <= end:
        # find the middle
        middle = (start + end) // 2
        # starting from the middle of the arr, if that value is the middle, return it
        if arr[middle] == target:
            return middle
        # if the target if greater then one side, ignore the left side
        elif arr[middle] < target:
            start = middle + 1
        else: 
            end = middle - 1
    return -1
        
    


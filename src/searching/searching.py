def linear_search(arr, target):
    # going through the loop of the arr 
    for i in range(len(arr)):
        # if the target is present in the array return it
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # first item in the arr
    start = 0
    # last item in the arr
    end = len(arr) - 1

    # A loop that will continue while the start is less than or equal to the end
    while end >= start:
        # find the middle by averaging the start and end and dividing by 2
        middle = (start+ end) // 2
        # guess is the middle index needed to retreive the target with the index from the arr
        guess = arr[middle]
        # if the guess is equal to the target, the middle index is correct and will be returned
        if guess == target:
            return middle
        # if guess is greater than the target, our arr is in halves and every value on the left is gone
        if guess > target:
            # it would - 1 because new END will be value BEFORE the middle
            end = middle - 1
        # if guess is lesser than the target, our arr is in halves and every value on the right is gone
        else:
            # it would be + 1 because new START would be AFTER the middle
            start = middle + 1

    return -1  # not found

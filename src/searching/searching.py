def linear_search(arr, target):
    # Your code here
    if len(arr) is not 0:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) is not 0:
        lowest = 0
        highest = len(arr) - 1
        return binary_search_helper(arr, target, highest, lowest)
    else:
        return -1


def binary_search_helper(arr, target, highest, lowest):
    mid_range = ((lowest + highest) / 2).__round__()

    if arr[mid_range] < target:
        return binary_search_helper(arr, target, highest, mid_range)
    elif arr[mid_range] > target:
        return binary_search_helper(arr, target, mid_range, lowest)
    else:
        if arr[mid_range] == target:
            return mid_range
        else:
            return -1
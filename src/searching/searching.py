def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    beg_i = 0
    end_i = len(arr) - 1
    
    found = False
    while beg_i <= end_i and not found:
        mid_i = (beg_i + end_i) // 2
        
        if arr[mid_i] == target:
            found = True
            return mid_i
        else:
            if arr[mid_i] > target:
                end_i = mid_i - 1
            else:
                beg_i = mid_i + 1

    return -1  # not found

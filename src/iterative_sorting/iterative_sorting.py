# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    # loop through the array until it has no longer made 
    #   any swaps
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            # if out of order, swap them
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                swapped = True
            #otherwise keep going
            else:
                continue

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    # check if empty
    if not arr:
        return arr
    #check if a max value has been passed
    if not maximum:
        maximum = arr[0]
        for item in arr:
            # check if there is a neg value in the array and if not
            # check and update the max value if needed.
            if item < 0:
                return "Error, negative numbers not allowed in Count Sort"
            if item > maximum:
                maximum = item

    # set the size of the bucket arry to the max value + 1
    buckets = [0] * (maximum + 1)
    # add all values to the appropriate buckets
    for item in arr:
        buckets[item] += 1
    return_array = []
    # loop through the buckets to find non empty ones
    for i in range(len(buckets)):
        if buckets[i]:
            # add the index to the return array for each count in the
            # bucket slot.
            for x in range(buckets[i]):
                return_array.append(i)
    arr = return_array

    return arr
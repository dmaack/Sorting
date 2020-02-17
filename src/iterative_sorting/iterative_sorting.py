# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range( cur_index + 1, len(arr)): # need to compare cur_index + 1 because we want to compare everything after the first position
            if arr[j] < arr[smallest_index]:
                smallest_index = j 




        # TO-DO: swap
        temp = arr[cur_index] # temp variable to store on the first index
        arr[cur_index] = arr[smallest_index] # then we change what was arr index or 1 to be what is in arr inex of 2
        arr[smallest_index] = temp # then store arr index of 2 into the temp variable
        



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)): # as i goes down
        for j in range(0, len(arr)-i-1): # so does j - avoid hitting the sorted portion of the array
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j +1]
                arr[j +1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
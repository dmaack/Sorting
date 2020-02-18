# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements # where to push my values into from 2 sorted arrays
    # TO-DO
    #look at the smallest value in input array
    #if the value in the first array is less than the second array -> push that value to merger_arr
    #if the value in the first array is greater than the second array -> push the value of the second array into merger_arr
    #once one array is drained of values, you can push the remaining values of the other array into merged array since sorted already
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

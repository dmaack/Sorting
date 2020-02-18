# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements # where to push my values into from 2 sorted arrays
    # TO-DO
    #look at the smallest value in input array
    #while there are values we need to look at 
    #if the value in the first array is less than the second array -> push that value to merger_arr
    #if the value in the first array is greater than the second array -> push the value of the second array into merger_arr
    #once one array is drained of values, you can push the remaining values of the other array into merged array since sorted already
    arrA_index = 0
    arrB_index = 0
    merged_index = 0 

    while arrA_index < len(arrA) and arrB_index < len(arrB): 
        if arrA[arrA_index] > arrB[arrB_index]:
            merged_arr[merged_index] ==  arrB[arrB_index]
            merged_index + 1
            arrB_index + 1
        elif arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_index] ==  arrA[arrA_index]
            merged_index + 1
            arrA_index + 1
    
    for a in arrA:
        arrA_index = a
        if arrA_index < len(arrA):
            merged_arr[merged_index] == arrA[a]
            a + 1
    
    for b in arrB:
        arrB_index = b
        if arrB_index < len(arrB):
            merged_arr[merged_index] == arrB[b]
            b + 1

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

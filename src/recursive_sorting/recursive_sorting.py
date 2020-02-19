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
            merged_arr[merged_index] =  arrB[arrB_index]
            merged_index = merged_index + 1
            arrB_index = arrB_index + 1
        else:
            merged_arr[merged_index] =  arrA[arrA_index]
            merged_index = merged_index + 1
            arrA_index = arrA_index + 1
    
    while arrA_index < len(arrA):
        merged_arr[merged_index] = arrA[arrA_index]
        merged_index = merged_index + 1
        arrA_index = arrA_index + 1
    
    while arrB_index < len(arrB):
        merged_arr[merged_index] = arrB[arrB_index]
        merged_index = merged_index + 1
        arrB_index = arrB_index + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # break up the unsorted array in half, repeatedly, until you are left with sub arrays with the length of 1 or empty - slice?
        # use recursion to reach the point of sub arrays of empty or length of 1 == to our base case for recursion rule?
    # once separated, use the merge function I created above     

    if len(arr) <= 1: # base case
        return arr
    arrA = arr[:len(arr)//2] 
    arrB = arr[len(arr)//2:]

    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)
    return merge(arrA, arrB)
    # return arr


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

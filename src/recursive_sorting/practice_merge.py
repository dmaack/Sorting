import math

arrA = [3, 7, 10, 11, 12 , 13]
arrB = [2, 6, 8]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
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

print(merge(arrA, arrB))

def merge_sort( arr ):
    if len(arr) <= 1: # base case
        return arr
    arrA = arr[:len(arr)//2]
    arrB = arr[len(arr)//2:]
    print(arrA, arrB)

    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)
    return merge(arrA, arrB)
    # return arr

print(merge_sort([10, 24, 76, 73, 1, 9]))
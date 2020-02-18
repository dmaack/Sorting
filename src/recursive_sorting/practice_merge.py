arr1 = [2, 3, 6, 7]
arr2 = [1, 4, 5]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
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

print(merge(arr1, arr2))
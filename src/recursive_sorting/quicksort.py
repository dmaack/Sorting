# Decide on a base case
# Find the pivot point
# partition our data to the left and right  of the pivot
# left -> smaller than pivot, right -> larger than pivot
# What if they're the same size as the pivot? Just pick one? >=
# repeat, recurse

my_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: # Handleing > or =
            right.append(item)

    return left, pivot, right # returning a tuple

def quick_sort(data):
    if data == []: # base case
        return data
    
    left, pivot, right = partition(data) # assigning a tuple

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(my_list)) # [1, 2, 3, 5, 6, 7, 8, 9]

# is the a good recursice sorting algorithm?
    # worst = O(n^2) -- thats pretty bad
# whats the right one to use?
    # it depends on the scenerio


# Algorithm
"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
"""
# TO-DO: complete the helper function below to merge 2 sorted arrays

# Pseudocode from https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    while (len(arrA) > 0 and len(arrB) > 0):
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
        else:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.remove(arrA[0])
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.remove(arrB[0])

    return merged_arr


arr_main = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]
# arr_1 = [1, 2, 4, 5, 8]
# arr_2 = [0, 3, 6, 7]
# print(arr_2[0:int(len(arr_2)/2)])
# print(arr_2[int(len(arr_2)/2):])
# print(merge(arr_1, arr_2))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    first_half = arr[0:int(len(arr)/2)]
    second_half = arr[int(len(arr)/2):]
    # use recursion
    first = merge_sort(first_half)
    second = merge_sort(second_half)
    return merge(first, second)


print(merge_sort(arr2))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

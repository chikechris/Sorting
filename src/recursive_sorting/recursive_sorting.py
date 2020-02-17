# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math
def merge( arrA, arrB ):

   sorted_arr = []
 
   while len(arrA) and len(arrB) != 0:
       if arrA[0] <= arrB[0]:
           sorted_arr.append(arrA.pop(0))
       else:
          sorted_arr.append(arrB.pop(0))
   return [sorted_arr, arrA, arrB]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if (len(arr) < 2):
        return arr
    n = math.ceil(len(arr)/2)
    arr1 = arr[0:n ]
    arr2 = arr[n: len(arr)]
    print(arr1, arr2)
    # TO-DO
# this recursively divides each array into half
    return merge(merge_sort(arr1), merge_sort(arr2))




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

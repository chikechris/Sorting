# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math
def merge( arrA, arrB ):

   sorted_array = []
 
   while len(arrA) and len(arrB) != 0:
       if arrA[0] <= arrB[0]:
           sorted_array.append(arrA.pop(0))
       else:
          sorted_array.append(arrB.pop(0))
   return [sorted_array, arrA, arrB]


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


# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     # TO-DO
#     if len(arr)>1:
#         middle = len(arr)//2
#         left_half = arr[:middle]
#         right_half = arr[middle:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i=0
#         j=0
#         k=0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k]=left_half[i]
#                 i=i+1
#             else:
#                 arr[k]=right_half[j]
#                 j=j+1
#             k=k+1

#         while i < len(left_half):
#             arr[k]=left_half[i]
#             i=i+1
#             k=k+1

#         while j < len(right_half):
#             arr[k]=right_half[j]
#             j=j+1
#             k=k+1

#     return arr


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

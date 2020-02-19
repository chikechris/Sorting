# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     current_index = i
    #     smallest_index = current_index
    #     # TO-DO: find next smallest element
    #     for j in range(current_index, len(arr)):
    #         if(arr[smallest_index] > arr[j]):
    #             smallest_index = j
    #     (arr[current_index], arr[smallest_index]) = (
    #         arr[smallest_index], arr[current_index])

    for i in range(0, len(arr) - 1):  # loop for num of elements in arr
        small_index = i    # small_index held in i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[small_index]: # compares if value at index j is smaller
                small_index = j   # stores j as smaller index
        (arr[i], arr[small_index]) = (arr[small_index], arr[i])  #swap value of smallest and i
    
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # print(arr)
    sorted = False
    while not sorted:
        swap = False
        for i in range(0, len(arr)-1):
            if(arr[i+1] < arr[i]):
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                swap = True
        if not swap:
            sorted = True
    return arr


# STRETCH: implement the Count Sort function below

    def counting_sort(arr):
        count = [0 for i in range(200)]
        print(len(count))
        for i in range(len(arr)):
            if arr[i] < 0:
                return "Error, negative numbers not ok in Count Sort"
            count[arr[i]] += 1

        for i in range(200):
            if i != 0:
                count[i] = count[i] + count[i-1]

        output = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            output[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1
        return output
    print(count_sort(arr1))


'''
This is a modified version of the 'Sort and search' task simplified 
for testing purposes.

'''       
#=========================== LINEAR SEARCH ============================================

def linear_search(arr, number):
    for i, element in enumerate(arr):
        if element == number:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found



#=========================== INSERTION SORT ============================================

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


#=========================== BINARY SEARCH ============================================

def binary_search(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1



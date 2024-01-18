#!/usr/bin/env python3
# merge-sort.py

"""
merge sort implementation
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # call the merge sort recursively for the left and right subarrays
        merge_sort(left)
        merge_sort(right)

        # initialize pointer for the left and right subarrays and main array
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+= 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # copy the remaining elements of the left subarray
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # copy the remaining elements of the right subarray
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    print("unsorted array:", arr)
    print("merge sorted array:",  merge_sort(arr))

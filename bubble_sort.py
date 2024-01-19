#!/usr/bin/python3

"""
    bubble sort implementation

    average case: O(n^2)
    worst case: O(n^2)
    best case: O(n) 
"""
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    print("Original arr: ", arr)
    print("Array after bubble sort: ", bubble_sort(arr))

#!/usr/bin/python3

"""
quick sort algorithm
best case: O(nlogn)
worst case: O(n^2)
"""
def quicksort(arr):
    """
    A function to implement quicksort algorithm
    """
    n = len(arr)
    mid = n // 2
    if n < 2:
        return arr
    else:
        pivot = arr[mid]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
if __name__ == '__main__':
    arr = [int(i)for i in input().split()]
    print("original arr:",arr)
    print("after quicksort:", quicksort(arr))

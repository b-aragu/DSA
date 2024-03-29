#!/usr/bin/python3

def insertion(arr):
    """
    insertion sort
    """
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while arr[j] > temp and j >=0:
      arr[j + 1] = arr[j]
      arr[j] = temp
      j -= 1
      arr[j + 1] = temp
  return arr  

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    print("original array:", arr)
    print(insertion(arr))

#!/usr/bin/python3
# selection sort implementation

def selection(arr):
    sub = []
    while arr!= []:
        min_ = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_]:
                min_ = i
        sub.append(arr.pop(min_) if len(arr) > 0 else arr[0])
    return sub
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    print(arr)
    print(selection(arr))

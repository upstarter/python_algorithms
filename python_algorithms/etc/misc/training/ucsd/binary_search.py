# Uses python3
import sys
import math

def binary_search(arr, low, high, x):
    if high >= low:

        mid = math.floor(low + ((high - low) // 2))
        # If element is present at the middle itself
        if arr[mid] == x:

            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1




# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n+1]
    # print(data,n,m, a, len(a)-1)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, len(a)-1, x), end = ' ')

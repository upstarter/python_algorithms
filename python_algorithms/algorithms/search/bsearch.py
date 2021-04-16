data = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5

# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


# Iterative Binary Search
def binary_search_iter(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return low - 1
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print binary_search_iter(data, 5)
print binary_search_recursive(data, 5, 0, len(data) - 1)

# JUMP SEARCH FOR INFINITE STREAM
# Search an infinite list of words in sorted order for an index corresponding to a word as input
# given an infinite list ["apple", "banana", "cat", "dog", ...] we have a class A where A.get(2) # => "cat" write a function to return the index for the word given as input to the function like so:
#
# A.get_index("cat") # => 2
# you can use A.get() but not python the .index() for sequences

import bisect


def inf_bsearch(endless_haystack, needle):

    if endless_haystack[0] == needle:
        return 0

    i = 1
    hay = endless_haystack[i]
    while hay < needle:  # this is O(log n) where n is the index of the element
        i = 2 * i
        hay = endless_haystack[i]

    # from the loop before the element is between i and i // 2
    return bisect.bisect_left(endless_haystack, needle, i // 2, i)

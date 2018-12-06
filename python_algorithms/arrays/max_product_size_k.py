
# Python 3 program to find the maximum
# product of a subarray of size k.

# This function returns maximum product
# of a subarray of size k in given array,
# arr[0..n-1]. This function assumes
# that k is smaller than or equal to n.
def findMaxProduct(arr, n, k) :

    # Initialize the MaxProduct to 1,
    # as all elements in the array
    # are positive
    MaxProduct = 1
    for i in range(0, k) :
        MaxProduct = MaxProduct * arr[i]

    prev_product = MaxProduct

    # Consider every product beginning
    # with arr[i] where i varies from
    # 1 to n-k-1
    for i in range(1, n - k + 1) :
        curr_product = (prev_product // arr[i-1]) * arr[i+k-1]
        MaxProduct = max(MaxProduct, curr_product)
        prev_product = curr_product


    # Return the maximum product found
    return MaxProduct

arr1 = [1, 5, 9, 8, 2, 4, 1, 8, 1, 2]
k = 6
n = len(arr1)
print (findMaxProduct(arr1, n, k) )
k = 4
print (findMaxProduct(arr1, n, k))

arr2 = [2, 5, 8, 1, 1, 3]
k = 3
n = len(arr2)

print(findMaxProduct(arr2, n, k))

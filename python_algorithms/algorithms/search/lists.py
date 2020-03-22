# kadanes algo, O(n) time, O(1) space
def max_subarray_sum(arr: [int]) -> int:
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


print(max_subarray_sum([-2, 4, 5, -1, 0]))

# Python program of a space
# optimized DP solution for
# 0-1 knapsack problem.

# val[] is for storing maximum
# profit for each weight
# wt[] is for storing weights
# n number of items
# W maximum capacity of bag
# mat[2][W+1] to store final result


def DPKnapSack(val, wt, n, W):

    # matrix to store final result
    mat = [[0 for i in range(W + 1)] for i in range(2)]
    # iterate through all items
    i = 0
    while i < n:  # one by one traverse
        # each element
        j = 0  # traverse all weights j <= W

        # if i is odd that means until
        # now we have an odd number of
        # elements so we store the result
        # in the 1th indexed row
        if i % 2 == 0:
            while j < W:  # check for each value
                j += 1
                if wt[i] <= j:  # include element
                    mat[1][j] = max(val[i] + mat[0][j - wt[i]], mat[0][j])
                else:  # exclude element
                    mat[1][j] = mat[0][j]

        # if i is even that means until
        # now we have an even number
        # of elements, so we store the
        # result in the 0th indexed row
        else:
            while j < W:
                j += 1
                if wt[i] <= j:
                    mat[0][j] = max(val[i] + mat[1][j - wt[i]], mat[1][j])
                else:
                    mat[0][j] = mat[1][j]
        i += 1
    # Return mat[0][W] if n is
    # odd, else mat[1][W]
    if n % 2 == 0:
        return mat[0][W]
    else:
        return mat[1][W]


# A dynamic programming algorithm for the 0-1 knapsack problem.
def Knapsack01(v, w, W):
    n = len(v) - 1

    c = []  # create an empty 2D array c
    for i in range(n + 1):  # c[i][j] = value of the optimal solution using
        temp = [0] * (W + 1)  # items 1 through i and maximum weight j
        c.append(temp)

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i] <= j:  # if item i will fit within weight j
                if (
                    v[i] + c[i - 1][j - w[i]] > c[i - 1][j]
                ):  # add item i if value is better
                    c[i][j] = v[i] + c[i - 1][j - w[i]]  # than without item i
                else:
                    c[i][j] = c[i - 1][j]  # otherwise, don't add item i
            else:
                c[i][j] = c[i - 1][j]
    return c[n][W]  # final value is in c[n][W]

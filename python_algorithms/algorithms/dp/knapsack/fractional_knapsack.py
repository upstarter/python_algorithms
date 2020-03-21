"""Return maximum value of items and their fractional amounts.

(max_value, fractions) is returned where max_value is the maximum value of
items with total weight not more than capacity.
fractions is a list where fractions[i] is the fraction that should be taken
of item i, where 0 <= i < total number of items.

value[i] is the value of item i and weight[i] is the weight of item i
for 0 <= i < n where n is the number of items.

capacity is the maximum weight.
"""


def fractional_knapsack(value, weight, capacity):
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions


n = int(input("Enter number of items: "))
value = input("Enter the values of the {} item(s) in order: ".format(n)).split()
value = [int(v) for v in value]
weight = input(
    "Enter the positive weights of the {} item(s) in order: ".format(n)
).split()
weight = [int(w) for w in weight]
capacity = int(input("Enter maximum weight: "))

max_value, fractions = fractional_knapsack(value, weight, capacity)
print("The maximum value of items that can be carried:", max_value)
print("The fractions in which the items should be taken:", fractions)

# A greedy algorithm for the fractional knapsack problem.
# Note that we sort by v/w without modifying v or w so that we can
# output the indices of the actual items in the knapsack at the end
def KnapsackFrac(v, w, W):
    order = bubblesortByRatio(v, w)  # sort by v/w (see bubblesort below)
    weight = 0.0  # current weight of the solution
    value = 0.0  # current value of the solution
    knapsack = []  # items in the knapsack - a list of (item, faction) pairs
    n = len(v)
    index = 0  # order[index] is the index in v and w of the item we're considering
    while (weight < W) and (index < n):
        if (
            weight + w[order[index]] <= W
        ):  # if we can fit the entire order[index]-th item
            knapsack.append((order[index], 1.0))  # add it and update weight and value
            weight = weight + w[order[index]]
            value = value + v[order[index]]
        else:
            fraction = (W - weight) / w[
                order[index]
            ]  # otherwise, calculate the fraction we can fit
            knapsack.append((order[index], fraction))  # and add this fraction
            weight = W
            value = value + v[order[index]] * fraction
        index = index + 1
    return (knapsack, value)  # return the items in the knapsack and their value


# sort in descending order by ratio of list1[i] to list2[i]
# but instead of rearranging list1 and list2, keep the order in
# a separate array
def bubblesortByRatio(list1, list2):
    n = len(list1)
    order = range(n)
    for i in range(n - 1, 0, -1):  # i ranges from n-1 down to 1
        for j in range(0, i):  # j ranges from 0 up to i-1
            # if ratio of jth numbers > ratio of (j+1)st numbers then
            if ((1.0 * list1[order[j]]) / list2[order[j]]) < (
                (1.0 * list1[order[j + 1]]) / list2[order[j + 1]]
            ):
                temp = order[j]  # exchange "pointers" to these items
                order[j] = order[j + 1]
                order[j + 1] = temp
    return order

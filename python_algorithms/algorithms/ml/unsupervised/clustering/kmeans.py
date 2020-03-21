# Import Library
from sklearn.cluster import KMeans

# Assumed you have, X (attributes) for training data set and x_test(attributes)
# of test_dataset
# Create KNeighbors classifier object model
k_means = KMeans(n_clusters=3, random_state=0)
# Train the model using the training sets and check score
model.fit(X)
# Predict Output
predicted = model.predict(x_test)


# FUNCTIONAL STYLE
from itertools import accumulate


def iterate(f, x):
    return accumulate(repeat(x), lambda fx, _: f(fx))


def k_means(points, k):
    initial_means = random.smaple(points, k)
    return iterate(partial(new_means, points), initial_means)


# 10 iters
means = take(10, kmeans(points, 5))

# until convergence
means = until_convergence(k_meanses(points, 5))


def until_convergence(it):
    prev = None
    while True:
        value = next(it)
        if value == prev:
            raise StopIteration
        yield value
        prev = value


def until_convergence(it):
    return acccumulate(it, no_repeat)


def no_repeat(prev, curr):
    if prev == curr:
        raise StopIteration
    else:
        return curr

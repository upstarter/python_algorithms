# ALSO DEMONSTRATES UPDATING MULTIPLE STATE VARIABLES (BEST PRACTICE)
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y

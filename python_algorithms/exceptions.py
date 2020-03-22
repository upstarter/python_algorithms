# Ensure variable is defined
try:
    x
except NameError:
    x = None


# Test whether variable is defined to be None
if x is None:
    print("some fallback operation")
else:
    print("some operation with: ", x)

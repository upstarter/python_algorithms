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


# Conditionals

## If
age = 18
if age >= 18:
    print(("is an adult"))
elif age >= 12:
    print("is a young adult")
elif age >= 3:
    print("child")
else:
    print("not an adult")

## Ternary
old_enough = "Adult" if age >= 21 else "Under 21"

## While
while age < 50:
    print("not old enough")
    age += 1

# Boolean Logic & Short Circuiting
1 and print(1)
0 and print(0)  # never prints (0, None, False)

1 or print(1)  # never prints
0 or print(0)  # prints 0

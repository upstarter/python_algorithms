# Uses python3
import sys

def fib_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        val = (previous + current) % 10
        previous, current = current, val

    return current

if __name__ == '__main__':
    n = int(input())
    print(fib_last_digit(n))

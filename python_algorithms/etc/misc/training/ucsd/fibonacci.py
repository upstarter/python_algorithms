# find nth fib
def calc_fib(n):
    a = [0,1]
    if n >= 2:
        for i in range(1, n+1):
            a.append(a[-1] + a[-2])
    return a[n]

def last_digit_fib(n):
    a = [0,1]
    if n >=2:
        for i in range(1,n+1):
            a.append((a[-1] + a[-2]) % 10)
    return a[n]

if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))

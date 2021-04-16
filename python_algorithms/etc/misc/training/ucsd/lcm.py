# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def compute_lcm(x, y):
   lcm = (x*y)//gcd_euclid(x,y)
   return lcm

def gcd_euclid(a,b):
  if b == 0:
      return a
  a_prime = a % b
  return gcd_euclid(b, a_prime)


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(compute_lcm(a, b))

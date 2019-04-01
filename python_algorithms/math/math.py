import math

## LOGARITHMS
log2 = math.log(x, 2.0)
log2 = math.log2(x)   # python 3.4 or later

# float in - int out If all you need is the integer part of log base 2 of a
# floating point number, math.frexp() could be pretty efficient:
log2int_slow = int(math.floor(math.log(x, 2.0)))
log2int_fast = math.frexp(x)[1] - 1

# Python frexp() calls the C function frexp() which just grabs and tweaks the
# exponent.  Python frexp() returns a tuple (mantissa, exponent). So [1] gets
# the exponent part. For integral powers of 2 the exponent is one more than you
# might expect. For example 32 is stored as 0.5x2⁶. This explains the - 1 above.
# Also works for 1/32 which is stored as 0.5x2⁻⁴.

# int in - int out If both input and output are integers, the integer method
# .bit_length() could be even more efficient:

log2int_faster = x.bit_length() - 1

# - 1 because 2ⁿ requires n+1 bits. This is the only option that works for very
# large integers, e.g. 2**10000.  All the int-output versions will floor the log
# toward negative infinity, so log₂31 is 4 not 5.

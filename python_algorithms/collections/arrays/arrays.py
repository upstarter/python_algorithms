# numpy arrays
import numpy as np
from pprint import pprint

arr_a = np.array([3, 6, 9])
arr_b = arr_a/3 # Performing vectorized (element-wise) operations
print(arr_b)

arr_ones = np.ones(4)
print(arr_ones)
# [ 1.  1.  1.  1.]
multi_arr_ones = np.ones((3,4)) # Creating 2D array with 3 rows and 4 columns
print(multi_arr_ones)
# [[ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]]

# One extremely notable aspect of NumPy is the manner in which it extends
# Python’s list indexing functionality—especially with multidimensional arrays.
# To illustrate, make a simple two-dimensional array and try some experiments:\
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
#=> array([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12]])

# Select row 1
print(a[1])
#=> array([5, 6, 7, 8])

# Select column 1
print(a[:,1])
#=> array([ 2, 6, 10])

# Select a subregion and change it
print(a[1:3, 1:3])
#=> array([[ 6, 7], [10, 11]])

a[1:3, 1:3] += 10
print(a)
#=> array([[ 1, 2, 3, 4], [ 5, 16, 17, 8], [ 9, 20, 21, 12]])

# Broadcast a row vector across an operation on all rows
a + [100, 101, 102, 103]
#=> array([[101, 103, 105, 107], [105, 117, 119, 111], [109, 121, 123, 115]])
print(a)
#=> array([[ 1, 2, 3, 4], [ 5, 16, 17, 8], [ 9, 20, 21, 12]])

# Conditional assignment on an array
print(np.where(a < 10, a, 10))
#=> array([[ 1, 2, 3, 4],

# python array
import array as arr
a = arr.array("I",[1,2,3])

# Type  code	C Type	Python Type	Minimum size in bytes
# 'b'	signed char	int	1
# 'B'	unsigned char	int	1
# 'u'	Py_UNICODE	Unicode character	2
# 'h'	signed short	int	2
# 'H'	unsigned short	int	2
# 'i'	signed int	int	2
# 'I'	unsigned int	int	2
# 'l'	signed long	int	4
# 'L'	unsigned long	int	4
# 'q'	signed long long	int	8
# 'Q'	unsigned long long	int	8
# 'f'	float	float	4
# 'd'	double	float	8

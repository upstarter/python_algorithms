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

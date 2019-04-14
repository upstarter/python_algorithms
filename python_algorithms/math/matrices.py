import numpy as np
# MULTIPLICATION
x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
x * y
#=> array([[ 2,  6], [15, -5]])
x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
x * y
#=> matrix([[17,  1], [28,  1]])

# CROSS PRODUCT
x = np.array([0,0,1])
y = np.array([0,1,0])

np.cross(x,y)
#=> array([-1,  0,  0])

np.cross(y,x)
#=> array([1, 0, 0])

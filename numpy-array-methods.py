# Numpy Array Methods

import numpy as np

d = np.array([1, 2, 3])

# append() function
d = np.append(d, [7, 8, 9])
print(d)

# insert(array_name, array_index, array2_name) function
d = np.insert(d, 2, [4, 5, 6])
print(d)

# delete(array_name, array_index, array_axis) function
d = np.array([[1, 2, 3],
               [4, 5, 6]])
print(np.delete(d, 0, 0))
print(np.delete(d, 1, 0))
print(np.delete(d, 0, 1))
print(np.delete(d, 1, 1))
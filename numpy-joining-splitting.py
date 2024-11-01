# Concatonating, Joining, Stacking and Splitting of Numpy Arrays

import numpy as np

f1 = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 0]])
f2 = np.array([[15, 14, 13, 12, 11],
              [20, 19, 18, 17, 16]])

# concatonate() function is used to concatonate the numpy arrays
f = np.concatenate((f1, f2), axis = 0)
print(f)
# If axis = 0, we concatonate the rows
# If axis = 1, we concatonate the columns

# stack() function is used to add a new dimension to the numpy array
f = np.stack((f1, f2))
print(f)
f = np.hstack((f1, f2))  # hstack() function concatonates on axis 1
print(f)
f = np.vstack((f1, f2))  # vstack() function concatonates on axis 0
print(f)

f3 = np.array([[1, 2, 3, 4, 5, 6],
              [6, 7, 8, 9, 0, 11],
              [15, 14, 13, 12, 11, 10],
              [20, 19, 18, 17, 16, 21]])

# split(array_name, no_of_splits, axis) function is used to split the numpy array
f3 = np.split(f3, 6, axis = 1)
print(f3)
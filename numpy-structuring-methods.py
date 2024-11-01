# Numpy Structuring Methods

import numpy as np


e = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])
print(e.shape)
# reshape(collections, lists, elements per list) function only returns the changed array without changing original size
print(e.reshape(5, 4)) 
print(e.reshape(20, 1))
print(e.reshape(20, ))
print(e.reshape(1, 20))
print(e.reshape(2, 10))
print(e.reshape(2, 5, 2))
print(e.reshape(5, 2, 2))

# resize(lists, ) method returns nothing and directly changes the original array
e.resize(5, 4)

# flatten() method a copy of a numpy array in 1-D version
#   e = e.flatten()
print(e.flatten())

# ravel() method also works like flatten() but returns the actual array in 1-D version
#   e = e.ravel()
print(e.ravel())
# We can also use flat. Eg., e.flat

# transpose() method returns the transposed array (swapping the axes)
# print(e.transpose())
print(e.T) # T is the shorthand for transpose()

# swapaxes() method swaps the axes of the array
print(e.swapaxes(0, 1))
# transpose() swaps the entire array while swapaxes() swaps the axes specified
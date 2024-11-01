import numpy as np
# Numpy provides a lot of mathematical functions to work with arrays
# Numpy arrays are faster than python lists
# Numpy arrays are more memory efficient than python lists
# Numpy arrays are more convenient to work with than python lists
# Numpy arrays are more powerful than python lists
# Numpy arrays are more versatile than python lists
# Numpy arrays are more optimized than python lists
# Numpy arrays are more flexible than python lists
# Numpy arrays are more reliable than python lists
# Numpy arrays are more scalable than python lists
# Numpy arrays are more readable than python lists
# Numpy arrays are more maintainable than python lists
# Numpy arrays are more reusable than python lists
# Numpy arrays are more consistent than python lists
# Numpy arrays are more predictable than python lists
# Numpy arrays are more robust than python lists
# Numpy arrays are more secure than python lists
# Numpy arrays are more stable than python lists
# Numpy arrays are more user-friendly than python lists


# Create a numpy array
a = np.array([1, 2, 3, 4, 5, 6]) 
print("a : \n", a)
print(type(a))  # array type
print(a[2])
print(a[1:5])
print(a[1:5:2])

# Create multi-dimensional numpy array
a_multi = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("a_multi : \n", a_multi)
print(a_multi[0, 2]) # element of the first array in multi-dimensional array
print(a_multi.shape) # dimensionality of the array
print(a_multi.ndim) # number of dimensions of an array
print(a_multi.size) # amount of elements in array
print(a_multi.dtype) # data type of an array

a_multi2 = np.array([[[1, 2, 3, 1],
                      [4, 5, 6, 1],
                      [7, 8, 9, 1]],
                    [[10, 11, 12, 1],
                     [14, 15, 16, 1],
                     [18, 19, 20, 1]]
                    ])
print("a_multi2 : \n", a_multi2)
print(a_multi2[1, 0, 2]) # element of the second array in multi-dimensional array
print(a_multi2.shape) 
print(a_multi2.ndim)
print(a_multi2.size)
print(a_multi2.dtype)
# Mathematical Operations in Numpy
# It is more like working with vectors and matrices than python lists

import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
# Converting lists to numpy arrays
a1 = np.array(l1)
a2 = np.array(l2)
print(l1 * 5)  # Multiplying lists with scalar(n) gives n times the same list as output
print(a1 * 5)  # Multiplying numpy arrays with scalar(n) gives new array with output.
print(l2 * 3)
print(a2 * 3)
print(l1 + l2)  # Adding lists gives a new list including elements from l1 and l2
print(a1 + a2)  # Adding numpy arrays gives a new array with output as sum of individual elements.
# print(l1 + 4)  # Gives error that it can only concatenate list (not "int") to list
print(a2 + 4)
print(a1 / a2)
print(a1 - a2)

b1 = np.array([1, 2, 3])
b2 = np.array([[4],
               [5]])
print(b1 + b2) # Output is in (2, 3) shape format
print(b1 * b2)
print(b1 / b2)
print(b1 - b2)
b3 = np.array([[4, 5],
               [6, 7]])
# print(b1 + b3)  # Error as operands could not be broadcast together with shapes (3,) (2,2)

# Numpy also has built-in mathematical functions
a = np.array([[2, 4, 6],
              [1, 3, 5]])
print(np.sqrt(a))
print(np.cbrt(a))
print(np.exp(a))
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.log(a))
print(np.log2(a))
print(np.log10(a))
# Static Typing in Numpy
import numpy as np

b = np.array([[1, 2, 3],
              [4, "hello", 6],
              [7, 8, 9]
            ])
print(b)
print(b.dtype) # <U21 - String with less than 21 characters. Data type of array is now a String.
print(type(b[0][0])) # b[0][0] = 1 but <class 'numpy.str_'> not numpy integer
print(b[0][0].dtype) # character of length 1

b2 = np.array([[1, 2, 3],
              [4, "5", 6],
              [7, 8, 9]], dtype = np.int32)
# If we have a number stored as string in an integer array, we can change it to integer by specifying dtype of array
print(b2.dtype)
print(type(b2[0][0]))
print(b2[0][0].dtype)

d = {1, 'A', 3, 'e'}
b3 = np.array([[1, 2, 3],
              [4, d, 6],
              [7, 8, 9]])
print(b3.dtype) # since dictionary(d) is not a primitive data type, hence dtype of array is object
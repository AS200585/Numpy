# Generating different types of Arrays in Numpy

import numpy as np


# Create an numpy array of same value
c = np.full((4, 4), 7)
print("c : \n",c)

# Create an numpy array of zeros
c2 = np.zeros((4, 3, 2))
print("c2 : \n",c2)

# Create an numpy array of ones
c3 = np.ones((6, 2, 4))
print("c3 : \n", c3)

# Create an empty numpy array. np.empty() function allocates the space without initializing values
c4 = np.empty((4, 4, 4))
print("c4 : \n", c4)

# Create an numpy array to generate values for plotting in a range
c5 = np.arange(0, 155, 3) # values from 0 to 155 with a difference of 3
print("c5 : \n", c5)

# Create an numpy array to generate n number of values for a given range
c6 = np.linspace(0, 100, 29) 
print("c6 : \n", c6)
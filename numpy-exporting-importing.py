# Importing and Exporting files in Numpy

import numpy as np

# Saving a numpy array to a file
i = np.array([14, 53, 356, 4562, 243, 2462, 7467, 3752, 2255, 276735, 36762562, 252])
np.save('numpy-array', i)
# Loading a numpy array from a file
i = np.load('numpy-array.npy')
print(i)

# Saving numpy array to a csv file
np.savetxt('numpy-array.csv', i, delimiter = ",")
# Loading numpy array from a csv file
i = np.loadtxt('numpy-array.csv', delimiter = ",")
print(i)
# Numpy Aggregate Functions
# Numpy aggregate functions can be used to perform statistical operations

import numpy as np

g = np.array([[2, 3, 4, 5, 6, 7],
              [8, 12, 9, 10, 13, 11],
              [14, 19, 18, 17, 16, 15],
              [26, 28, 23, 29, 20, 27]])

print(g.max())  # Maximum element
print(g.min())  # Minimum element
print(g.sum())  # Sum of elements
print(g.mean())  # Mean of elements
print(g.std())  # Standard Deviation of elements
print(np.median(g))  # Median of elements
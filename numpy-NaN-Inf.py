# NaN(Not a Number) and Inf(Infinity) in Numpy

import numpy as np


# nan is used to fill up enpty spaces within a dataset with the value 'nan' to indicate the given index is empty
print(np.nan)

# inf is used to show infinity value for infinity conditions like division by zero etc. instead of throwing an exception
print(np.inf)

print(np.isnan(np.nan)) # To check if given value is NaN or not
print(np.isinf(np.inf)) # To check if given value is Inf or not

print(np.sqrt(-1))
print(np.array([10]) / 0)
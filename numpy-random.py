# Generating random values with Numpy

import numpy as np

# randint(range, array_shape) function is used to generate random integers
h1 = np.random.randint(100)
print(h1)
h1 = np.random.randint(100, size = (2, 3, 4)) # Generates numpy array with random integers
print(h1)
h1 = np.random.randint(2, size = (2, 3, 4)) # Generates numpy array with integers 0 and 1
print(h1)
h1 = np.random.randint(30, 90, size = (2, 3, 4)) # Generates numpy array with random integers between 30 and 90
print(h1)

# binomial(no_of_tries, probablity, array_shape) function is used to generate binomial distribution values
h2 = np.random.binomial(15, p = 0.7, size = (5, 10))
print(h2)
# normal(mean, scale(std), array_shape) function is used to generate binomial distribution values
h2 = np.random.normal(loc = 170, scale = 10, size = (4, 9))
print(h2)
# uniform(low, high, array_shape) function is used to generate uniform distribution values
h2 = np.random.uniform(17, 39, size = (4, 9))
print(h2)
# poisson(lambda, array_shape) function is used to generate poisson distribution values
h2 = np.random.poisson(lam = 5, size = (4, 9))
print(h2)

# choice() function is used to generate random choices from a given numpy array
h2 = np.random.choice([10, 20, 30, 40, 50, 60, 70, 80], size = (4, 4))
print(h2)
# shuffle() function is used to shuffle the elements of a numpy array
h2 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
np.random.shuffle(h2)
print(h2)

# rand() function is used to generate random floats
h2 = np.random.rand(3, 13)
print(h2)
# randn() function is used to generate random floats with normal distribution
h2 = np.random.randn(9, 23)
print(h2)
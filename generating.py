import numpy as np
import time

# def GenerateRandom(array_sizes,seed=42):
#     random_arrays = []

#     # Set the seed for reproducibility
#     np.random.seed(seed)

#     # Generate 30 random arrays for each size and record sorting times
#     for size in array_sizes:
#         random_array = np.random.randint(0, 10000, size=size)
#         random_arrays.append(random_array)
    
#     return random_arrays

def GenerateRandom(array_size,seed=42):

    # Set the seed for reproducibility
    np.random.seed(seed)

    # Generate 30 random arrays for each size and record sorting times
    random_array = np.random.randint(0, 10000, size=array_size)
    
    return random_array

def GenerateRandomInc(array_sizes, seed=42):
    random_arrays = []

    # Set the seed for reproducibility
    np.random.seed(seed)

    # Generate 30 random arrays for each size and record sorting times
    for size in array_sizes:
        random_array = np.random.randint(0, 10000, size=size)
        random_array.sort()
        random_arrays.append(random_array)
    
    return random_arrays

def GenerateRandomDec(array_sizes, seed=42):
    random_arrays = []

    # Set the seed for reproducibility
    np.random.seed(seed)

    # Generate 30 random arrays for each size and record sorting times
    for size in array_sizes:
        random_array = np.random.randint(0, 10000, size=size)
        random_array = np.sort(random_array)[::-1]
        random_arrays.append(random_array)
    
    return random_arrays
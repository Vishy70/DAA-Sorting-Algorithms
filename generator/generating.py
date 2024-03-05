import numpy as np
import time

def GenerateRandom(array_size,seed=42):

    # Set the seed for reproducibility
    np.random.seed(seed)

    random_array = np.random.randint(0, 10000, size=array_size)
    
    return random_array

def GenerateRandomInc(array_size, seed=42):

    # Set the seed for reproducibility
    np.random.seed(seed)

    random_array = np.random.randint(0, 10000, size=array_size)
    random_array.sort()

    return random_array

def GenerateRandomDec(array_size, seed=42):

    # Set the seed for reproducibility
    np.random.seed(seed)

    random_array = np.random.randint(0, 10000, size=array_size)
    random_array = np.sort(random_array)[::-1]
    
    return random_array

def GenerateDuped(array_size, seed=42):

    common_element = np.random.randint(0, 10000)
    
    differing_index = np.random.randint(0, array_size)
    differing_element = np.random.randint(0, 10000)  
    while differing_element == common_element:
        differing_element = np.random.randint(0, 100)
    
    random_array = np.full(array_size, common_element)
    random_array[differing_index] = differing_element
    
    return random_array

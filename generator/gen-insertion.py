import numpy as np
import generating as generating
from generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

def Generate_Insertion_Best(array_size,seed=42):
    return GenerateRandomInc(array_size, seed)

def Generate_Insertion_Worst(array_size, seed=42):
    return GenerateRandomDec(array_size, seed)

def Generate_Insertion_Average(array_size, seed=42):
    return GenerateRandom(array_size, seed)
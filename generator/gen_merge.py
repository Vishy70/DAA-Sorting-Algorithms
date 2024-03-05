import numpy as np
import generator.generating as generating
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

def Generate_Merge_Best(array_size, seed=42):
    return GenerateRandom(array_size, seed)

def Generate_Merge_Worst(array_size, seed=42):
    return GenerateRandom(array_size, seed)
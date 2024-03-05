import numpy as np
import generator.generating as generating
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

def Generate_Heap_Best(array_size,seed=42):
    return GenerateRandomInc(array_size, seed)

def Generate_Heap_Worst(array_size, seed=42):
    return GenerateRandomDec(array_size, seed)
import numpy as np
import generator.generating as generating
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

def Generate_Quick2_Best(array_size, seed=42):
    return GenerateRandom(array_size, seed)

def Generate_Quick2_Worst(array_size, seed=42):
    return GenerateRandom(array_size, seed)
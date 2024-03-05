import numpy as np
import generator.generating as generating
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

def Generate_Quick1_Best(array_size, seed=42):
    return GenerateRandom(array_size, seed)

def Generate_Quick1_Worst(array_size, seed=42):
    return GenerateRandomInc(array_size, seed)
import numpy as np
import generator.generating as generating
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc, GenerateDuped

def Generate_Quick3_Best(array_size, seed=42):
    return GenerateRandomInc(array_size, seed)

def Generate_Quick3_Worst(array_size, seed=42):
    return GenerateDuped(array_size, seed)
import numpy as np
import time
import Algorithms
import generating
from Algorithms import Bubble_sort, Bubble_sort2, Insertion_sort, Merge_sort, Quick_sort1, Quick_sort2, Quick_sort3, Heap_sort, Radix_sort
from generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

#index-based ChooseSort
def ChooseSort(choice, arr):
    sorting_functions = {
        1: Bubble_sort,
        2: Bubble_sort2,
        3: Insertion_sort,
        4: Merge_sort,
        5: Quick_sort1,
        6: Quick_sort2,
        7: Quick_sort3,
        8: Heap_sort,
        9: Radix_sort
    }
    
    if choice in sorting_functions:
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")




def TestAllSortingAlgos():
    arr=[7,4,1,3,9,8,2]
    for i in range(1,10):
        anew=arr.copy(); #to ensure that arr wont be sorted for remaining cases
        #print("Unsorted array:", anew)
        ChooseSort(i,anew)
        print("Sorted array:", anew)
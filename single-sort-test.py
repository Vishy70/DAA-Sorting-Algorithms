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



def SortAny():
    array_string = input("Enter elements of the array separated by spaces: ")
    arr = list(map(int, array_string.split()))  
    print("Menu:\n1.Bubble Sort\n2.BubbleSort2\n3.InsertionSort\n4.MergeSort\n5.QuickSort1\n6.QuickSort2\n7.QuickSort3\n8.HeapSort\n9.RadixSort")
    choice = input("Enter choice:")
    ChooseSort(choice,arr)
    print("Sorted array:", arr)


